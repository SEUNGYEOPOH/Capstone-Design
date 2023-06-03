<template>
  <div id="total_wraper">
    <div class="left_wraper">
      <div id="top">
        <b-dropdown
          text="카메라 리스트"
          block
          class="l-2"
          menu-class="w-100"
        ><div class="column_wrap">
          <div class="column">
            <span>전체</span>
            <span>9</span>
          </div>
          <hr class="vertical_line">
          <div class="column" style="color: blue;">
            <span>녹화중</span>
            <span>6</span>
          </div>
          <hr class="vertical_line">
          <div class="column" style="color: red">
            <span>연결끊김</span>
            <span>3</span>
          </div>
        </div>
        </b-dropdown>
      </div>
      <div id="middle" style="background-color: white;">
        <b-input-group size="sm" class="mb-2">
          <b-form-input type="search" placeholder="카메라 검색"></b-form-input>
          <b-input-group-prepend is-text>
            <b-icon icon="filter-circle"></b-icon>
          </b-input-group-prepend>
        </b-input-group>
        <b-dropdown
          text="자치구 카메라 현황"
          block
          class="l-2"
          menu-class="w-100"
        >
          <div id="cctv"><a href="#">1번 지역 CCTV(127.0.0.1)</a></div>
          <div id="cctv"><a href="#">2번 지역 CCTV(127.0.0.1)</a></div>
          <div id="cctv"><a href="#">3번 지역 CCTV(172.22.23.81)</a></div>
          <div id="cctv"><a href="#">4번 지역 CCTV(127.0.0.1)</a></div>
          <div id="cctv"><a href="#">5번 지역 CCTV(172.22.23.215)</a></div>
          <div id="cctv"><a href="#">6번 지역 CCTV(127.0.0.1)</a></div>
          <div id="cctv"><a href="#">7번 지역 CCTV(172.22.22.90)</a></div>
          <div id="cctv"><a href="#">8번 지역 CCTV(172.22.22.91)</a></div>
          <div id="cctv"><a href="#">9번 지역 CCTV(127.0.0.1)</a></div>
        </b-dropdown>
      </div>
      <div id="bottom" style="height: 100%;"><img src="@/assets/crowdguardlogo.png" style="width: 98%"></div>
    </div>
    <div class="right_wraper">
      <!-- <div id="banner">
        <h4 class="banner_heading">banner 영역(추후 삽입 예정)</h4>
      </div>
      <hr class="custom_hr"> -->
      <div class="video_wraper">
        <div id="embed_video" style="width: 100%; height:auto; border: 2px solid; border-color: #5C6BC0;">
          <b-embed
            type="iframe"
            aspect="16by9"
            src="https://www.youtube.com/embed/GqOMgjUkbsI"
            allowfullscreen
          ></b-embed>
        </div>
      </div>
      <hr class="custom_hr">
      <div class="log table">
        <b-container>
          <datatableVue />
        </b-container>
      </div>
    </div>
  </div>
</template>

<script>
import datatableVue from '@/components/layouts/datatable.vue'
import Navbar from '../components/layouts/navbar.vue'


/* eslint-disable */
export default {
  name: 'Detect',
  components: {
    datatableVue,
    Navbar
  },
  data(){
    return{
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
.left_wraper{
  width: 25%;
  height: 100%;  
  float: left;
}
.right_wraper{
  float: left;
  width: 75%;
}
.column_wrap{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 60px;
}
.column{
  margin-bottom: 10px;
  height: 50px;
  float: left;
  padding: 0 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  font-weight: bolder;
}
.column span{
  display: block;
  font-size: large;
}
.vertical_line{
  border: none;
  border-left: 2px double black;
  height: 50px;
  margin: 0 10px;
  float: left;
}
#top{
  text-align: center;
}
#middle{
  background-color: #ffffff;
}
#cctv a{
  text-decoration: none;
  font-weight: bolder;
}
a:visited{
  color: rgb(85, 85, 85);
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
  width: 100%;
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