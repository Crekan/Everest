<template>
  <swiper
      :slides-per-view="1"
      :space-between="50"
      @swiper="onSwiper"
      @slideChange="onSlideChange"
  >
    <swiper-slide>
      <img src="../../../public/assets/img/slider-img1.png" alt="img1">
    </swiper-slide>
    <swiper-slide>
      <img src="../../../public/assets/img/slider-img1.png" alt="img1">
    </swiper-slide>
    <swiper-slide>
      <img src="../../../public/assets/img/slider-img1.png" alt="img1">
    </swiper-slide>
  </swiper>
</template>

<script>
import { Swiper, useSwiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';

export default {
  name: "SliderSwiperComponent",
  components: {
    Swiper,
    SwiperSlide,
  },

  setup() {
    const onSwiper = (swiper) => {
      console.log(swiper);
    };
    const onSlideChange = () => {
      console.log('slide change');
    };
    const swiper = useSwiper();
    return {
      onSwiper,
      swiper,
      onSlideChange,
    };
  },
}
</script>

<style scoped>
img {
  height: 550px;
}
</style>