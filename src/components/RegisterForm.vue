<template>
    <div class="login-container">
      <form @submit.prevent="registerUser">
        <div class="form-group">
          <i class="fa-solid fa-user"></i>
        <input type="text" name="username" v-model="username" placeholder="User name ..." required>
        </div>
        <div class="form-group">
        <i class="fa-solid fa-envelope"></i>
        <input type="email" name="email" v-model="email" placeholder="Enter Email ..." required>
      </div>
        <div class="form-group">
          <i class="fa-solid fa-lock"></i>
        <input type="password" name="password" v-model="password" placeholder="Password ..." required>
      </div>
        <button type="submit">Register</button>

      </form>
      <div id="ifWrong"></div>
    </div>
  </template>
  
  <script>
    
import axios from 'axios';
    axios.defaults.xsrfHeaderName = 'x-csrftoken'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.withCredentials = true
  export default {
    data() {
      return {
        username: '',
        email: '',
        password: '',
        csrftoken:'',
      }
    },
    mounted(){
      axios.get('http://localhost:8000/get_csrf_token')
      .then(response => {
        this.csrftoken = response.data.token;
        console.log(this.csrftoken);
      })
      .catch(error => {
        console.error(error);
      });
    },

    methods: {



      async registerUser() {
        console.log(this.csrftoken);
        try {
           await axios.post('http://localhost:8000/register_user/', {
            username: this.username,
            email: this.email,
            password: this.password,
            csrfmiddlewaretoken: this.csrftoken
          }
      );
      this.throwError(true);
      } catch(error) {this.throwError(false)}
    },

    async throwError(isValid) {
        switch(isValid) {
          case true: 
            document.getElementById("ifWrong").innerHTML="";
            break;
          case false:
            document.getElementById("ifWrong").innerHTML="User already exists or passwords don't match!"
            break;
        }
        
    }

  }
    }
  </script>

  <style scoped>

  .login-container {
    width: 30vw;
    align-self: center;
    border-radius: 10px;
  }
  .form-group{
    display: flex;
    align-items: center;
    flex-direction: row;
  
  }
  form {
    display: flex;
    flex-direction: column; 
    justify-content: center;
    
  }
  button {
   
    border-radius: 5px;
    background-color: rgba(100, 115, 163, 1);
    border-style: none;
    color: white;
    margin: 0.5rem;
    padding: 0.5rem;
  }

  button:hover {
    background-color:rgba(100, 115, 163, 0.8);
  }
  input {
    width: 100%;
    margin: 0.5rem;
    padding: 0.5rem;
    border-style: none;
  }

  #ifWrong {
    color: red;
  }

  </style>