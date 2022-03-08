<template>
    <div id="app">
      <Header/>
      <router-view/>
      <Footer/>
    </div>
</template>

<script>

import Header from "./components/Header";
import Footer from "./components/Footer";

export default {
  name: 'App',
  components: {
    Footer,
    Header,
  }
}
</script>

<style>
  @import "assets/css/StyleAll.css";
  @import "assets/css/manga_cart.css";
  @import "assets/css/auth.css";
  @import "assets/css/swipe_default.css";
  @import "assets/css/swiper.min.css";
  @import "assets/css/pagination.css";

#app{
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>
