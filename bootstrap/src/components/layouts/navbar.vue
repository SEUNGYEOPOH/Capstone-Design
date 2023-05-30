<template id="test">
    <div id = "header">
        <b-navbar id="test" toggleable="lg" type="dark" variant="info" >
            <b-navbar-brand style="font-size: 30px">Crowd Guard</b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
                <b-nav-item href="/">Map</b-nav-item>
                <b-nav-item href="/Detect">Detect</b-nav-item>
            </b-navbar-nav>
            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
                <b-nav-form>
                    <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
                    <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
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
.
<style>


.header{
    height: 1024px;
    width: 101px;
}
.nav-item{
    font-size: 20px;
    width : 101px;
}

/* .button{
    margin-left: auto;
} */
</style>