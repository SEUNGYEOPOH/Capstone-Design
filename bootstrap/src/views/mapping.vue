<template>
    <div id="container">

        <l-map
        :zoom="zoom"
        :center="center"
        :bounds="bounds"
        :max-bounds="maxBounds"
        :options="{ zoomControl: false }"
        style="height: 850px; width: 80%; margin: 0; padding :0; float: left;"
        >
        <l-tile-layer :url="url" />
        <l-marker v-for="marker in markers" :key="marker.id" :lat-lng="marker.coordinates" @click="goToDetect">
            <l-tooltip>{{ marker.title }}</l-tooltip>
        </l-marker>
        </l-map>
        <div id ="right_wrap">
            <div id = "top">
                <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=40&pause=1000&color=F7F6F6&background=25C30380&center=true&vCenter=true&width=400&height=250&lines=%F0%9F%9B%A1+Safety+%F0%9F%9B%A1" alt="Typing SVG" />
                <!--<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=40&duration=2500&pause=500&color=F7F6F6&background=FFAB20DF&center=true&vCenter=true&width=330&height=250&lines=%E2%9A%A0++caution+%E2%9A%A0" alt="Typing SVG" /> -->
                <!--<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=40&duration=1250&pause=250&color=F7F6F6&background=FF1914B1&center=true&vCenter=true&width=330&height=250&lines=%F0%9F%9A%A8++danger+%F0%9F%9A%A8" alt="Typing SVG" /> -->
            </div>
            <div id = "bottom">
              
            </div>
        </div>
        
    </div>

</template>



<!-- map display code-->
<script>

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
    
};
</script>
<style>
    #container{
        width :100%; 
        height: 100%;
        margin : 0; 
        padding : 0;
        right: 0; /* Align to the right side of the container */
        float: right;
        position: relative;
    }
    #right_wrap {
        width: 20%;
        height: 850px;
        position: absolute;
        right: 0; /* Align to the right side of the container */
    }
    #top{
        width : 100%;
        height : 250px;
        padding: 0;
        margin: 0;
    }
    #bottom{
        width : 100%;
        height : 250px;
        padding: 0;
        margin: 0;
        background-color: aqua;
    }

  
    

        
</style>