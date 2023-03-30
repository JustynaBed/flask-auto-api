<template>
  <div>
    <h1>Home v3</h1>
    <ul>
      <li v-for="auto in autos" :key="auto.id">
      BRABD: {{auto.brand}} MODEL: {{auto.model}} YEAR: {{auto.year}}
      </li>
    </ul>
    <form @submit.prevent="addAuto">
      <label>Brand:
        <input type="text" v-model="brand">
      </label>
      <label>Model:
        <input type="text" v-model="model">
      </label>
       <label>year:
        <input type="text" v-model="year">
      </label>
      <button type=submit>Add</button>
    </form>
  </div>
</template>

<script>
// import axios from 'axios'
import * as API from '../api'
export default {
  name: 'HomeApp',
  data () {
    return {
      autos: [],
      brand: '',
      model: '',
      year: ''
    } 
  },
  methods: {
      getAutos() {
      return API.fetchautos()
      .then(response => this.autos = response.data) 
    },
    addAuto () {
      return API.createAuto({
          brand: this.brand, 
          model: this.model, 
          year: this.year
      }).then(response => console.log(response))
    }
  },
  created () {
    this.getAutos()
  },
    mounted() {
    console.log('mounted', process.env.VUE_APP_API_URL)
  },
}
</script>