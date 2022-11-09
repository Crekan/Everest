<template>
  <main-layout-component>
    <main class="container">
      <div class="home">
        <slider-swiper-component/>
        <section class="catalog mt160">
          <h1 class="sc-title sc-title_mb48">Каталог</h1>
          <div class="catalog__content catalog__content_mt48">
            <catalog-item-component
                v-for="(category, idx) in catalog"
                :key="category[category.length - 1].id"
                :category="category[1]"
                :catalog="category[0]"
                :index="idx"
            />
          </div>
        </section>
        <section class="news mt160">
          <h1 class="sc-title sc-title_mb48">Новости</h1>
          <div class="news__content">
            <news-item-component
                v-for="(item, idx) in news"
                :key="item[item.length - 1].id"
                :item="item[item.length - 1]"
                :news="item"
                :index="idx"
            />
          </div>
        </section>
      </div>
    </main>
  </main-layout-component>
</template>

<script>

import {
  // ref,
  reactive,
  // toRefs,
  // isRef,
  // isReactive,
  // computed,
  // watch
  // onMounted,
    computed,
} from 'vue'

// import { useGetters } from 'vuex-composition-helpers'

import { useStore } from 'vuex'

import MainLayoutComponent from "@/js/layouts/MainLayoutComponent";
import SliderSwiperComponent from "@/js/components/SliderSwiperComponent";
import CatalogItemComponent from "@/js/components/HomePageComponents/CatalogItemComponent";
import NewsItemComponent from "@/js/components/HomePageComponents/NewsItemComponent";
// import axios from 'axios'

export default {
  name: "HomePage",
  components: {
    MainLayoutComponent,
    SliderSwiperComponent,
    CatalogItemComponent,
    NewsItemComponent,
  },
  setup() {
    const store = useStore()

    const catalog = computed(() => store.getters["Catalogs/getCatalogItems"])
    const news = reactive([
      [
        [
          "# Акзонобел",
          "# Интерьерные краски"
        ],
        {
          "alt": "img1",
          "date": "04.05.2022",
          "id": "0",
          "img": "/assets/img/HomePage/news-img1.png",
          "title": "Dulux Diamond Max Protect",
          "views": "121"
        }
      ],
      [
        [
          "# Bostik",
          "# Клей"
        ],
        {
          "alt": "img2",
          "date": "30.04.2022",
          "id": "1",
          "img": "/assets/img/HomePage/news-img2.png",
          "title": "Новинка! Быстросохнущий монтажный клей MAMUT",
          "views": "581"
        }
      ],
      [
        [
          "# АКЗОНОБЕЛЬ",
          "# Dulux"
        ],
        {
          "alt": "img3",
          "date": "20.04.2022",
          "id": "2",
          "img": "/assets/img/HomePage/news-img3.png",
          "title": "Сканер цвета Dulux — лидерам отрасли!",
          "views": "1 089"
        }
      ],
      [
        [
          "# Акция",
          "# Сайвер"
        ],
        {
          "alt": "img4",
          "date": "05.03.2022",
          "id": "3",
          "img": "/assets/img/HomePage/news-img4.png",
          "title": "Негорючие системы окраски КМ0 - Dulux Diamond Max Protect",
          "views": "1 821"
        }
      ]
    ])

    return {
      catalog,
      news,

      store,
    }
  }
}
</script>

<style scoped lang="scss">
.home {
  margin-top: 32px;
}

.catalog {
  &_y160 {
    margin: 160px 0;
  }

  &__content {
    display: grid;
    grid-template-columns: auto auto auto;
    gap: 32px 24px;

    &_mt48 {
      margin-top: 48px;
    }
  }
}

.news {
  &__content {
    display: flex;
  }
}

//@media screen and (max-width: 1350px) {
//  .catalog {
//    &__content {
//      grid-template-columns: auto auto;
//    }
//  }
//}
</style>