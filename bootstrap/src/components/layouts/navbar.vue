<template id="test">
    <div id = "header">
        <b-navbar id="test" toggleable="lg" navbar-skyblue bg-sky>
            <b-navbar-brand style="font-size: 40px; color: rgb(51, 178, 228); ">Crowd Guard</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
                <b-nav-item class = "test" href="/" style="text-align: center;">
             
                    <img src="@/assets/map.png" alt="" width="25" height="25" class="d-inline-block align-text-top">
                     Map
                </b-nav-item>
                <b-nav-item href="/Detect">
                
                    <img src="@/assets/cctv.png" alt="" width="25" height="25" class="d-inline-block align-text-top">
                   
                    Detect
                </b-nav-item>
            </b-navbar-nav>
            <!-- Right aligned nav items -->
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
    width : 101px;
    padding-right: 40px; 
}
.navbar-brand {
    margin-left: 25%;
    padding-right: 8%;
}

/* .button{
    margin-left: auto;
} */
</style> 

<script>
/* eslint-disable */
export default {
    name:"Navbar"
};
</script>
.
<style>


.header{
    height: 1024px;
    width: 101px;
}
.nav-item{
    font-size: 20px;
    width : 200px;
}
.b-button{
    height: 25%;
}
/* .button{
    margin-left: auto;
} */
</style>