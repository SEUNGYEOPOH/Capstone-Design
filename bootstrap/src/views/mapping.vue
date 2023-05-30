<template>
    <div id="container">
      <l-map
        :zoom="zoom"
        :center="center"
        :bounds="bounds"
        :max-bounds="maxBounds"
        :options="{ zoomControl: false }"
        style="height: 850px; width: 80%; margin: 0; padding: 0; float: left;"
      >
        <l-tile-layer :url="url" />
        <l-marker v-for="marker in markers" :key="marker.id" :lat-lng="marker.coordinates" @click="goToDetect">
          <l-tooltip>{{ marker.title }}</l-tooltip>
        </l-marker>
      </l-map>
      <div id="right_wrap">
        <div id="top">
          <img
            src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=40&pause=1000&color=F7F6F6&background=25C30380&center=true&vCenter=true&width=400%&height=300&lines=%F0%9F%9B%A1+Safety+%F0%9F%9B%A1" alt="Typing SVG" Align="center"/>
        </div>
        <div id = "middle">
                <div class="weather-wrap" v-if="weather.main">
                    <div class="location-box">
                        <div class="location">{{ weather.name }}, {{ weather.sys.country }}</div>
                        <div class="date">{{ dateBuilder() }}</div>
                    </div>
                    <div class="weather-box">
                        <div class="temp">{{ Math.round(weather.main.temp) }}℃</div>
                        <div class="weather">{{ weather.weather[0].main }}</div>
                    </div>
                </div>
            </div>
        <div id="bottom">
          <h3>This div displays table(state, location)</h3>
        </div>
      </div>
    </div>
  </template>
  
<script>
import { latLngBounds } from "leaflet";
import { LMap, LTileLayer, LMarker,LTooltip } from "vue2-leaflet";
export default {
    name: "SetBounds",
    components: {
        LMap,
        LTileLayer,
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
        ],
        api_key: "b2ad80802a9487acbc841a42bd558638",
        url_base: "https://api.openweathermap.org/data/2.5/",
        weather: {}
        };
    },
    created(){
        this.fetchWeatherByLocation("Yongsan")
    },
    methods: {
        goToDetect(){
            window.location.href = "/Detect";
        },
        fetchWeatherByLocation(location) {
            let fetchUrl = `${this.url_base}weather?q=${location}&units=metric&APPID=${this.api_key}`;
            fetch(fetchUrl)
                .then((res) => res.json())
                .then((results) => {
                this.weather = results;
            });
        },
        dateBuilder() {
            let d = new Date();
            let months = ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"];
            let days = ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"];
            let day = days[d.getDay()];
            let date = d.getDate();
            let month = months[d.getMonth()];
            let year = d.getFullYear();
            return `${year}년 ${month} ${date}일, ${day} `;
            }    
    },
    
};
</script>




<!-- map display code-->



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
        height : 300px;
        padding: 0;
        margin: 0;
        
    }
    #middle{
        width : 100%;
        height : 300px;
        padding: 0;
        margin: 0;
        background-color:skyblue;
    }
    #bottom{
        width : 100%;
        height: 250;
        padding: 0;
        margin: 0;
    }
    .location-box .location {
  color: #fff;
  font-size: 32px;
  font-weight: 500;
  text-align: center;
  text-shadow: 1px 3px rgba(0, 0, 0, 0.25);
}
.location-box .date {
  color: #fff;
  font-size: 20px;
  font-weight: 300;
  font-style: italic;
  text-align: center;
}
.weather-box {
  text-align: center;
}
.weather-box .temp {
  display: inline-block;
  padding: 10px 25px;
  color: #fff;
  font-size: 40px;
  font-weight: 50;
  text-shadow: 2px 4px rgba(0, 0, 0, 0.25);
  background-color: rgba(255, 255, 255, 0.25);
  border-radius: 16px;
  margin: 30px 0px;
  box-shadow: 2px 4px rgba(0, 0, 0, 0.25);
}
.weather-box .weather {
  color: #fff;
  font-size: 40px;
  font-weight: 50;
  font-style: italic;
  text-shadow: 2px 4px rgba(0, 0, 0, 0.25);
}
  
    

        
</style>