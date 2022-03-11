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
import axios from "axios";

export default {
  name: 'App',
  components: {
    Footer,
    Header,
  },
  beforeCreate() {
    this.$store.commit("initializeStore")
    const access = this.$store.state.access

    if (access){
      axios.defaults.headers.common['Authorization'] = "JWT" + access
    }else{
      axios.defaults.headers.common['Authorization'] = ''
    }
  }
}
</script>

<style>
  @import "assets/css/StyleAll.css";
  @import "assets/css/manga_cart.css";
  @import "assets/css/auth.css";
  @import "assets/css/swipe_default.css";
  @import "assets/css/swiper.min.css";

#app{
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>
