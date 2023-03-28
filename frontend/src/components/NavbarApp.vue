<template>
  <div>
    <navbar>
      <ul>
        <li>
          <router-link to="/">Home</router-link>
        </li>
             <li>
          <router-link to="/create">Create</router-link>
        </li>
      </ul>
    </navbar>
  </div>
</template>

<script>
export default {
  name: "NavbarApp"
}
</script>