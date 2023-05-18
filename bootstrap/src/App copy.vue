<template>
  <div id="whole_wraper">
    <div class="banner">
      <img src="">
    </div>
    <!-- <hr class="hrcss"></hr> -->
    <div class="table_wraper">
      <!-- iframe은 받아오는 데이터의 형태에 따라 변경해야함 -->
      <Iframe src="" >
        <img src="" style="width:100%;">
      </Iframe>
      <!-- <hr class="hrcss"></hr> -->
      <div class="log">
        <!-- 여기는 search bar태그 위치 -->
        <div class="search">
          <input type="text" style="color: deepskyblue;" placeholder="로그를 입력해주세요.">
          <button>검색</button>
        </div>
        <!-- <hr class="hrcss"></hr> -->
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Cam_No</th>
              <th>State</th>
              <th>date</th>
              <th>image url</th>
              <th>distance</th>
              <th>Area</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in student" :key="user.id">
              <td>{{ user.Id }}</td>
              <td>{{ user.cam_name }}</td>
              <td>{{ user.state }}</td>
              <td>{{ user.c_date }}</td>
              <td>{{ user.img_url }}</td>
              <td>{{ user.distance }}</td>
              <td>{{ user.area }}</td>
            </tr>
          </tbody>
        </table>
        <!-- pagination 영역 -->
        <v-pagination :length="6"></v-pagination>
      </div>    
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Iframe from './Iframe.vue';

export default {
  name: 'App',
  components:{
      Iframe
  },
  data() {
    return {
      student: []
    }
  },
  mounted(){
    this.fetchData();
  },
  methods: {
    fetchData(){
      this.$axios.get('awslecturedb.cfpwksovkphh.ap-northeast-2.rds.amazonaws.com/student') // 데이터를 불러올 엔드포인트를 입력
        .then(response => {
          this.users = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
}
</script>

<style>
.banner{
  padding-bottom: 10px;
}
.Iframe{
  width: auto;
}
/* #hrcss{
  color: deepskyblue;
  border: 1px;
} */
</style>
