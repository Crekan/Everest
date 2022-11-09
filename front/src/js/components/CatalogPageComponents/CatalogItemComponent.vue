<template>
  <div class="catalog__item">
    <div class="catalog__item-img">
      <img :src="item.img" alt="img">
    </div>
    <div class="catalog__item-title" >
      <h3>{{ item.name }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: "CatalogItemComponent",
  props: {
    item: Object,
  }
}
</script>

<style scoped>

</style>