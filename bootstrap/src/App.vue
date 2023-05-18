<template>
    <div id="map">
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

</style>