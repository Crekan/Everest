<template>
    <header-component/>
    <slot></slot>
    <footer-component/>
</template>

<script>
import HeaderComponent from "@/js/components/HeaderComponent";
import FooterComponent from "@/js/components/FooterComponent";

export default {
  name: "MainLayoutComponent",
  components: {
    HeaderComponent,
    FooterComponent,
  }
}
</script>

<style scoped>

</style>