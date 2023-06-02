<template>
    <div>
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
            <b-table :items="users" :fields="fields"></b-table>
            <b-pagination-nav pills size='lg' number-of-pages="numberOfPages" base-url="baseUrl" align="center"></b-pagination-nav>
        </b-container>
    </div>
</template>

<script>
import axios from 'axios';
/* eslint-disable */
export default {
    name: 'datatable',
    data() {
        return {
            users: [],
            fields: [
                { key: 'id', label: 'ID' },
                { key: 'cam_name', label: 'Cam_No' },
                { key: 'state', label: 'State' },
                { key: 'c_date', label: 'Date' },
                { key: 'distance', label: 'Distance' },
                { key: 'area', label: 'Area' },
                { key: 'img_url', label: 'Image URL' , formatter: 'imageLink'}
            ],
            currentPage: 1,
            pageSize: 20
        };
    },
    mounted() {
        this.fetchData();
    },
    methods: {
        fetchData() {
        axios.get('http://13.209.243.33:8000/api/WebcamDetect/')
            .then(response => {
            this.users = response.data; // 기존 코드
            console.log(response.data)
            // 아래 코드 추가
            if (Array.isArray(this.users)) {
                // users가 배열인 경우
                this.users = this.users.map(item => {
                    return {
                        id: item.id,
                        cam_name: item.cam_name,
                        state: item.state,
                        c_date: item.c_date,
                        distance: item.distance,
                        area: item.area,
                        img_url: item.img_url
                    };
                });
            } else {
                // users가 배열이 아닌 경우
                this.users = [];
            }
        })
        .catch(error => {
            console.log(error);
        });
    },
    imageLink(value){
        return `${value}`;
    }
    },
    computed: {
        numberOfPages(){
            return Math.ceil(this.users.count / this.pageSize);
        },
        baseUrl(){
            return window.location.href.split('?')[0] //현재페이지 URL에서 쿼리 파라미터를 제거하여 base URL을 생성
        }
    }
};
</script>