<template>
  <main-layout-component>
    <main class="container">
      <div class="catalog">
        <h1 class="sc-title sc-title_y">{{ catalog[catalog.length - 1].title }}</h1>
        <section class="catalog__content">
          <catalog-item-component
              v-for="item in catalog[0]"
              :item="item"
              :key="item.id"
          />
        </section>
      </div>
    </main>
  </main-layout-component>
</template>

<script>
import { useRouter, useRoute } from 'vue-router'

import {
  // ref,
  // reactive,
  // toRefs,
  // isRef,
  // isReactive,
  // computed,
  // watch
  // onMounted,
  // onUpdated,
  // computed,
} from 'vue'

import MainLayoutComponent from "@/js/layouts/MainLayoutComponent";
// import axios from "axios";
import { useStore } from "vuex";
import CatalogItemComponent from "@/js/components/CatalogPageComponents/CatalogItemComponent";

export default {
  name: "CatalogPage",
  setup() {
    const store = useStore()
    const router = useRouter()
    const route = useRoute()

    const catalog = store.getters["Catalogs/getCatalogItems"][route.params.id]

    return {
      catalog,

      router,
      route,
    }
  },
  components: {
    CatalogItemComponent,
    MainLayoutComponent
  },
}
</script>

<style scoped>

</style>