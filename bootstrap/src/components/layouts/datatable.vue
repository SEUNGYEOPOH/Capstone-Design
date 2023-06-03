<template>
    <div>
        <b-table :items="users" :fields="fields">
            <template v-slot:cell(img_url)="row">
            <img :src="row.value" alt="Image" style="width: 200px; height: auto;" />
            </template>
        </b-table>
        <b-pagination
            v-model="currentPage"
            pills
            :total-rows="totalRows"
            :per-page="pageSize"
            size="lg"
            align="center"
        ></b-pagination>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'DataTable',
    data() {
        return {
            users: [],
            fields: [
            { key: 'id', label: 'ID' },
            { key: 'cam_name', label: 'Cam_No' },
            { key: 'state', label: 'State' },
            { key: 'c_date', label: 'Date' },
            { key: 'count', label: 'Count' },
            { key: 'area', label: 'Area' },
            { key: 'img_url', label: 'Image URL' },
            ],
            currentPage: 1,
            pageSize: 20,
            totalRows: 0,
        };
        },
        mounted() {
        this.fetchData();
        },
        methods: {
        fetchData() {
            axios
            .get('http://13.209.243.33:8000/api/WebcamDetect/', {
                params: {
                page: this.currentPage,
                page_size: this.pageSize,
                },
            })
            .then(response => {
                this.users = response.data.results;
                this.totalRows = response.data.count;
            })
            .catch(error => {
                console.error(error);
            });
        },
        },
        watch: {
        currentPage() {
            this.fetchData();
        },
        pageSize() {
            this.fetchData();
        },
    },
};
</script>