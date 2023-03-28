<template>
  <div>
    <h1>Home</h1>
    <ul>
      <li v-for="auto in autos" :key="auto.id">{{auto.brand}}</li>
    </ul>
    <form @submit="addAuto">
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
    addAuto () {
      fetch('http://127.0.0.1:5000/api/v1/autos', {
        method: 'POST',
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          brand: this.brand, 
          model: this.model, 
          year: this.year
        })
      })
      .then(resp => resp.json())
      .catch(error => console.log(error))
    },
    getAutos() {
      fetch('http://127.0.0.1:5000/api/v1/autos', {
        method: 'GET',
        headers: {
          "Content-Type": "application/json"
        }
      })
      .then(resp => resp.json())
      .then(data => 
      this.autos = data.data
      // console.log(data.data)
      )
      .catch(error => console.log(error))
    }
  },
  created () {
    this.getAutos()
  }
}
</script>