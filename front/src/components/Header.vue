<template>
<header class="header">
    <div class="wrapper">
    <nav>
      <input type="checkbox" id="show-search">
      <input type="checkbox" id="show-menu">
      <label for="show-menu" class="menu-icon"><i class="fas fa-bars"></i></label>
      <div class="content">
      <div class="logo"><a href="#">HLove</a></div>
        <ul class="links">
          <li><a href="">Главная</a></li>
          <li><a href="#">Новое</a></li>
          <li>
            <a href="#" class="desktop-link">Популярное</a>
            <input type="checkbox" id="show-features">
            <label for="show-features">Features</label>
            <ul>
              <li><a href="#">Drop Menu 1</a></li>
              <li><a href="#">Drop Menu 2</a></li>
              <li><a href="#">Drop Menu 3</a></li>
              <li><a href="#">Drop Menu 4</a></li>
            </ul>
          </li>
          <li><a href="#">О нас</a></li>
          <li><a href="#" @click="showAuthInfo">Войти</a></li>
          <li><a href="#">Регистрация</a></li>
          <li><a href="#">Профиль</a></li>
          <li><a href="#">Выйти</a></li>
        </ul>
      </div>
      <label for="show-search" class="search-icon"><i class="fas fa-search"></i></label>
      <form action="#" class="search-box">
        <input type="text" placeholder="Поиск..." required>
        <button type="submit" class="go-icon"><i class="fas fa-long-arrow-alt-right"></i></button>
      </form>
    </nav>
    </div>
  <div class="main-banner bg bg1"></div>
  </header>
  <SignIn
      v-if="IsInfo"
      @closeAuth="closeInfo"
  />

</template>

<script>
import SignIn from "../views/SignIn";

export default {
  name: "Header",
  components: {
    SignIn,
  },
  methods:{
    showAuthInfo(){
      this.IsInfo=true;
    },
    closeInfo(){
      this.IsInfo=false;
    }
  },
  data(){
    return{
      IsInfo: false
    }
  }
}
</script>

<style scoped>
.wrapper{
  background: #111;
  position: fixed;
  width: 100%;
  z-index: 999999;
}
</style>