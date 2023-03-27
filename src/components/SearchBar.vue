<template>
<div class="search-bar">
        <div class="search-container">
        <i class="fa-solid fa-magnifying-glass"></i>
        <input id="SearchInput" type="text" placeholder="Search"> 
    </div>

    <div class ="account-container">
        <i class="fa-solid fa-right-to-bracket"></i>
        Login
    </div>
    </div>


</template>

<style scoped>
.search-bar {
    display: flex;
    justify-content: space-between;
    
    
}
 .search-container {
 margin-left: 5rem;
 }

 .account-container {
margin-right: 5rem;
 }
 input {
    margin-left: 0.3rem;
    
    border-style: none;
    border-bottom: 1px solid gray;
 }
</style>

<script>
export default{}
</script>