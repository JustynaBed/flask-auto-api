<template>
  <div>
    <h1>Vue App </h1>
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
