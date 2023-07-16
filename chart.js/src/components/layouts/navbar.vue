<template id="test">
    <div id = "header">
        <b-navbar id="test" toggleable="lg" navbar-skyblue bg-sky>
            <b-navbar-brand style="font-size: 40px; color: rgb(51, 178, 228);">
                <img src="@/assets/crowdguardlogo.png" style="height: 40px; width:auto;">
                CROWD GUARDIAN
            </b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
            
            <b-navbar-nav>
                <b-nav-item href="/">
                    <div style="display: flex; align-items: center;">
                        <img src="@/assets/map.png" width="25" height="25" class="d-inline-block align-text-top">
                        <span>Map</span>
                    </div>
                </b-nav-item>
                <b-nav-item href="/Detect">
                    <div style="display: flex; align-items: center;">
                        <img src="@/assets/cctv.png" width="25" height="25" class="d-inline-block align-text-top">
                        <span>Detect</span>
                    </div>
                </b-nav-item>
            </b-navbar-nav>

            <b-navbar-nav class="ml-auto" navbar-skyblue bg-skyblue>
                <b-nav-form navbar-skyblue bg-skyblue>
                    <b-form-input size="md" class="mr-sm-2" placeholder="Search"></b-form-input>
                    <b-button variant="outline-info" type="submit">Search</b-button>
                </b-nav-form>                
            </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>    
</template>   
<script>
/* eslint-disable */
export default {
    name:"Navbar"
};
</script>

<style>
.header{
    height: 1024px;
    width: 101px;
}
.nav-item{
    font-size: 25px;
    width : 180px;
    padding-right: 40px;
    display: flex; 
}
.navbar-brand {
    margin-left: 25%;
    padding-right: 8%;    
}
</style> 

