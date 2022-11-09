<template>
  <figure class="catalog__category">
    <div class="catalog__category-img catalog__category-img_mb25">
      <img :src="category.img" :alt="category.alt">
    </div>
    <div class="catalog__category-title catalog__category-title_mb24" @click="router.push(`/catalog/${category.id}`)">
      <span>{{ category.title }}</span>
    </div>
    <figcaption class="catalog__category-description">
      <p
          class="catalog__category-description-item"
          v-for="(it, idx) in catalog"
          :key="idx"
      >{{ it.name }}</p>
    </figcaption>
  </figure>
</template>

<script>
import { useRouter, useRoute } from 'vue-router'

export default {
  name: "CatalogItemComponent",
  props: ['category', 'catalog', 'index'],
  setup() {
    const router = useRouter()
    const route = useRoute()

    return {
      router,
      route,
    }
  },
}
</script>

<style scoped lang="scss">
.catalog {
  &__category {
    width: 424px;
    background: #E8EFF5;
    border-radius: 4px;
    padding: 38px 32px 32px;

    &-img {
      max-width: 100px;

      &_mb25 {
        margin-bottom: 25px;
      }
    }

    &-title {
      display: inline-block;
      font-weight: 800;
      font-size: 21px;
      line-height: 24px;
      text-transform: uppercase;
      color: #0E192E;
      cursor: pointer;

      &_mb24 {
        margin-bottom: 24px;
      }
    }

    &-description {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
    }

    &-description-item {
      background: #FFFFFF;
      border-radius: 4px;
      padding: 8px 12px;
      font-weight: 400;
      font-size: 14px;
      line-height: 21px;
    }
  }
}
</style>