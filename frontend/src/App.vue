<template>
  <div>
    <NavbarApp/>
    <router-view/>
  </div>
</template>

<script>
import NavbarApp from './components/NavbarApp.vue'

export default {
  name: 'App',
  components: {
    NavbarApp
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
