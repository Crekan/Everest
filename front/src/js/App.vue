<template>
  <router-view/>
</template>

<script>

export default {
  name: 'App',
  components: {}
}
</script>

<style lang="scss">
*,
*::before,
*::after {
  box-sizing: border-box;
}

body,
h1,
h2,
h3,
h4,
p,
ul[class],
ol[class],
li,
figure,
figcaption,
blockquote,
dl,
dd {
  margin: 0;
  color: #0E192E;
}

a {
  text-decoration: none;
  color: #0E192E;
}

span,
p,
a,
h1,
h2,
h3,
h4,
h5,
h6 {
  color: inherit;
}

body {
  min-height: 100vh;
  scroll-behavior: smooth;
  text-rendering: optimizeSpeed;
  font-family: 'Onest', sans-serif;
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 24px;
  overflow-x: hidden;
}

ul, ol {
  list-style: none;
  padding: 0;
}

img {
  max-width: 100%;
  display: block;
}

article > * + * {
  margin-top: 1em;
}

input,
button,
textarea,
select {
  font: inherit;
}

/*ОБНУЛЯЮЩИЕ СТИЛИ*/

.container {
  max-width: 1320px;
  width: 100%;
  margin: 0 auto;
}

.d-flex {
  display: flex;
}

.align-center {
  align-items: center;
}

.justify-center {
  justify-content: center;
}

.col {
  flex-direction: column;
}

.sc-title {
  font-weight: 800;
  font-size: 48px;
  line-height: 52px;
  text-transform: uppercase;
  color: #0E192E;

  &_mb48 {
    margin-bottom: 48px;
  }

  &_y {
    margin-top: 68px;
    margin-bottom: 48px;
  }
}

.mt160 {
  margin-top: 160px;
}

@media screen and (max-width: 1350px) {
  .container {
    padding: 0 10px;
  }
}
</style>
