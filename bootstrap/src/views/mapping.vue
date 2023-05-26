<template>
    <div>
        <l-map
        :zoom="zoom"
        :center="center"
        :bounds="bounds"
        :max-bounds="maxBounds"
        :options="{ zoomControl: false }"
        style="height: 92.4vh; width: 100%"
        >
        <l-tile-layer :url="url" />
        <l-marker v-for="marker in markers" :key="marker.id" :lat-lng="marker.coordinates" @click="goToDetect">
            <l-tooltip>{{ marker.title }}</l-tooltip>
        </l-marker>
        </l-map>
    </div>
</template>

<script>
import L from 'leaflet'
/* eslint-disable */
// import { latLngBounds, latLng } from "leaflet";
import { latLngBounds } from "leaflet";
import { LMap, LTileLayer, LGeoJson, LMarker,LTooltip } from "vue2-leaflet";

export default {
    name: "SetBounds",
    components: {
        LMap,
        LTileLayer,
        LGeoJson,
        LMarker,
        LTooltip
    },
    data() {
        return {
        zoom: 13,
        center: [0, 0],
        bounds: latLngBounds([
            [37.715133, 126.734086],
            [37.413294, 127.269311]
        ]),
        maxBounds: latLngBounds([
            [37.715133, 126.734086],
            [37.413294, 127.269311]
        ]),
        url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        // leafmarker: latLng(37.56667,126.97806),
        markers: [
            {
                id: 1,
                title: "용산구",
                coordinates: [37.53138497, 126.979907],
            },
            {
                id: 2,
                title: "강남구",
                coordinates: [37.49664389, 127.0629852],
            },
            {
                id: 3,
                title: "중구",
                coordinates: [37.56014356,126.9959681],
            },
            {
                id: 4,
                title: "서초구",
                coordinates: [37.47329547,127.0312203],
            },
            {
                id: 5,
                title: "마포구",
                coordinates: [37.55931349,126.90827],
            }
        ]
        };
    },
    methods: {
        goToDetect(){
            window.location.href = "/Detect";
        }
    },
    mounted(){
        const map = L.map('map',{ zoomControl: false });
        map.dragging.disable();        
    }
};
</script>