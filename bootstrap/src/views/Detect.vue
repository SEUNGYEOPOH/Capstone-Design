<template>
  <div id="app">
    <div class="total_wraper">
      <div id="banner">
        <h4 class="banner_heading">banner 영역(추후 삽입 예정)</h4>
      </div>
      <hr class="custom_hr">
      <div class="video_wraper">
        <div id="embed_video">
          <b-embed
            type="iframe"
            aspect="4by3"
            src="https://www.youtube.com/embed/GqOMgjUkbsI"
            allowfullscreen
            style="width: 1000px; height:590px; border: 2px solid; border-color: #5C6BC0;"
          ></b-embed>
        </div>
      </div>
      <hr class="custom_hr">
      <div class="log table">
        <b-container>
          <h3 style="padding-left: 150px;">[Detection Log]</h3>
          <b-input-group class="searchbar">
            <b-form-input 
            type="search"
            size="xl" 
            placeholder="로그를 검색해주세요"
            ></b-form-input>
            <b-button variant="outline-primary">검색</b-button>
          </b-input-group>
          <!-- <datatableVue/> -->
          <b-table striped hover :items="items" :fields="fields"></b-table>
          <b-pagination-nav pills size='lg' number-of-pages="10" base-url="#" align="center"></b-pagination-nav>
        </b-container>
      </div>
    </div>
  </div>
</template>

<script>
// import DatatableVue from './components/views/datatable.vue'
import Navbar from '../components/layouts/navbar.vue'

/* eslint-disable */
export default {
  name: 'Detect',
  components: {
    // DatatableVue
    Navbar
  },
  data(){
    return{
      fields: ['ID','Cam_No','State','date','imageUrl','distance','Area'],
      items: [
        {isActive: true,ID:1,Cam_No:1,State:'안전',date:'2023-05-11',imageUrl:'www.naver.com',distance:'53㎡',Area:'용산구'},
        {isActive: false,ID:2,Cam_No:1,State:'주의',date:'2023-05-11',imageUrl:'http://image2.jpg',distance:'21㎡',Area:'마포구'},
        {isActive: true,ID:3,Cam_No:1,State:'안전',date:'2023-05-11',imageUrl:'http://image3.jpg',distance:'66㎡',Area:'성북구'},
        {isActive: false,ID:4,Cam_No:1,State:'위험',date:'2023-05-11',imageUrl:'http://image4.jpg',distance:'44㎡',Area:'서대문구'},
        {isActive: true,ID:5,Cam_No:1,State:'주의',date:'2023-05-11',imageUrl:'http://image5.jpg',distance:'36㎡',Area:'영등포구'},
        {isActive: false,ID:2,Cam_No:1,State:'주의',date:'2023-05-11',imageUrl:'http://image2.jpg',distance:'21㎡',Area:'마포구'},
        {isActive: true,ID:3,Cam_No:1,State:'안전',date:'2023-05-11',imageUrl:'http://image3.jpg',distance:'66㎡',Area:'성북구'},
        {isActive: false,ID:4,Cam_No:1,State:'위험',date:'2023-05-11',imageUrl:'http://image4.jpg',distance:'44㎡',Area:'서대문구'},
        {isActive: true,ID:5,Cam_No:1,State:'주의',date:'2023-05-11',imageUrl:'http://image5.jpg',distance:'36㎡',Area:'영등포구'}
      ],
      currentPage: 1,
      perPage: 10,
      totalRows: 10
    }
  }
}
</script>

<style>
.total_wraper{
  width: 1200px;
  margin-left: auto;
  margin-right: auto;
}
#banner{
  background: linear-gradient(lightCyan, skyBlue, deepSkyBlue);

  height: 100px;
  width: 100%;
  border: 5px groove;
  padding: 30px;
  margin-left: auto;
  margin-right: auto;
}
.log table{
  width: 1000px;
  background-color: #ffffff;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}
.banner_heading{
  text-align: center;
}
.custom_hr{
  width: 1000px;
  height: 10px;
  background-image: linear-gradient(to right, #eee, #777, #eee);
  border: none;
  margin: 10px;
  margin-left: auto;
  margin-right: auto;
}
.video_wraper{
  margin-left: auto;
  margin-right: auto;
}
.searchbar{
  padding-left: 150px;
  padding-right: 150px; /* 넓이를 조절하고자 하는 크기로 변경해주세요 */
  padding-bottom: 20px;
}
</style>