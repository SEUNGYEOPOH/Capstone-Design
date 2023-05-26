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
            <!-- <datatableVue/> -->
            <b-table :items="users" :fields="fields"></b-table>
            <b-pagination-nav pills size='lg' number-of-pages="10" base-url="#" align="center"></b-pagination-nav>
        </b-container>
    </div>
</template>

<script>
import axios from 'axios';
import { BTable } from 'bootstrap-vue';
/* eslint-disable */
export default {
name: 'DataTable',
components: {
    BTable,
    axios
},
data() {
    return {
    users: [],
    fields: [
        { key: 'id', label: 'ID' },
        { key: 'cam_name', label: 'Cam_No' },
        { key: 'state', label: 'State' },
        { key: 'c_date', label: 'Date' },
        { key: 'img_url', label: 'Image URL' },
        { key: 'distance', label: 'Distance' },
        { key: 'area', label: 'Area' }
    ]
    };
},
mounted() {
    this.fetchData();
},
methods: {
    fetchData() {
    axios.get('http://api.com/users')
        .then(response => {
        this.users = response.data;
        })
        .catch(error => {
        console.log(error);
        });
    }
}
};
</script>