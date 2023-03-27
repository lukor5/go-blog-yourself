<template>
    <div class="post-container">
      <ul>
        <div class="single-post-container" v-for="post in posts" :key="post.id">
            <div class="post-details">
          <h2>{{ post.title }}</h2>
          <h3>{{ post.author }}</h3>
        
        </div>
          {{ post.content }}
        </div>
      </ul>
    </div>
  </template>
  
  <style scoped >
        .post-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            
        }

        .post-details {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
        }

      .single-post-container {
        max-width: 20rem;
        word-wrap: break-word;
        padding: 2rem;
        margin: 2rem;
        border-left: 1px solid gray;
            border-bottom: 1px solid black;
      }
    </style>

  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        posts: []
      }
    },
    mounted() {
      axios.get('http://localhost:8000/posts/')
        .then(response => {
          this.posts = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
  </script>