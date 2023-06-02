<template>
    <div>
        <!-- <h2 id="title">서울시 자치구 CCTV현황</h2> -->
        <l-map
            :zoom="zoom"
            :center="center"
            @update:zoom="zoomUpdated"
            @update:center="centerUpdated"
            @update:bounds="boundsUpdated"
            style="width: 100%; height: 800px;"
        ><l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>  
        <l-layer-group v-for="(layer, index) in booklayers" :key="index" :name="layer.name">
            <l-circle-marker v-for="(marker, index) in layer.markers" :key="index" :lat-lng="marker.latlng"
                :color="marker.color" :id="marker.id" @click="markerOnClick">
            </l-circle-marker>
            <l-marker
                v-for="marker in markers"
                :key="marker.name"
                :lat-lng="marker.latLng"
            ></l-marker>    
        </l-layer-group>
        </l-map>

        <!-- Modal EMPTY -->
        <div class="modal left fade" id="emptymodal" tabindex="-1">
            <div class="modal-dialog" role="document">
                <div class="modal-content"></div>
            </div>
        </div>
    </div>
</template>
<script>
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { latLng, Icon } from 'leaflet';
import markerShadowImg from 'leaflet/dist/images/marker-shadow.png';
import markerRetinaImg from 'leaflet/dist/images/marker-icon-2x.png';
import seoulmap from '../assets/seoulmap.geojson'
import Navbar from '../components/layouts/navbar.vue'

import { LMap, LTileLayer, LLayerGroup, LCircleMarker } from 'vue2-leaflet';

/* eslint-disable */
export default {
    name:"map",
    components:{
        LMap,
        LTileLayer,
        LLayerGroup,
        LCircleMarker,
        Navbar,
        seoulmap
    },
    data () {
    return {
        url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        attribution:
            '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        zoom: 13,
        center: latLng[37.51867,126.97806],
        bounds: null,
        markerImg: markerImg,
        markerShadowImg: markerShadowImg,
        markers:[
            {
                name:'jongro',
                latLng:[37.59491732,126.9773213]
            },
            {
                name:'yongsan',
                latLng:[37.53138497,126.979907]
            }
        ],
        locationlayers: [
            {
            name: '자치구',
            markers: [
                { latlng: [37.59491732,126.9773213], color: 'red',id: '종로구' },
                { latlng: [37.56014356,126.9959681], color: 'red',id: '중구' },
                { latlng: [37.53138497,126.979907], color: 'red',id: '용산구' },
                { latlng: [37.55102969,127.0410585], color: 'red',id: '성동구' },
                { latlng: [37.54670608,127.0857435], color: 'red',id: '광진구' },
                { latlng: [37.58195655,127.0548481], color: 'red',id: '동대문구' }
            ]
            }
        ]
        };
    }, methods: {
        zoomUpdated (zoom) {
        this.zoom = zoom;
        },
        centerUpdated (center) {
        this.center = center;
        },
        boundsUpdated (bounds) {
        this.bounds = bounds;
        },
        markerOnClick(e) {
        const id = e.target.options.id
        this.modalContent = `${id}CCTV리스트`;
        this.$refs.emptymodal.modal('show');  // Vue 인스턴스에서 ref로 설정한 DOM 요소 접근
        this.$refs.map.setView(e.target.getLatLng());
        } 
    },created(){
        const geojsonLayer = L.geoJSON(seoulmap).addTo(this.$refs.map);
        this.$refs.map.addLayer(geojsonLayer);
    },
    mounted() {
        /* eslint-disable */
        const map = L.map('map',{ zoomControl: false , attributionControl: false}).setView([37.56667,126.97806], 11);
        // 서울의 위경도 경계 37.715133, 126.734086부터 37.413294, 127.269311
        // GeoJSON 데이터를 가져와서 변수에 저장
        map.dragging.disable();
        delete Icon.Default.prototype._getIconUrl;
        Icon.Default.mergeOptions({
            iconRetinaUrl: markerRetinaImg,
            iconUrl: markerImg,
            shadowUrl: markerShadowImg,
        });  
    }
}
</script>
<style>
/* #map {
    height: 80%;
    width: 100%;
} */
#title{
    background-color:transparent;
    margin-top: auto;
}    
</style>
