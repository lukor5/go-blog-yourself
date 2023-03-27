<template>
 
   <div class="RegisterModal">
  
  </div>
  <SearchBar></SearchBar>
  <PostList></PostList>
</template>

<script>
import PostList from './components/PostList.vue'
import SearchBar from './components/SearchBar.vue'


export default {
  name: 'App',
  components: {
    PostList,
    SearchBar,
    
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  color: #2c3e50;
  margin-top: 60px;
}


.RegisterModal {
  visibility: hidden;
}

</style>
