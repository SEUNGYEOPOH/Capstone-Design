<template>
    <div id="all_map">
        <Navbar />
        <router-view></router-view>
    </div>    
</template>
<script>
import Navbar from './components/layouts/navbar.vue'

/* eslint-disable */
export default {
    name: 'app',
    components:{
        Navbar
    }
}
</script>

<style>
.all_map{
    margin : 0;
    float: left;
    padding: 0;
    position: relative;
}
.router-view-container {
    width: 1390px;
    height: 850px;
}
</style>