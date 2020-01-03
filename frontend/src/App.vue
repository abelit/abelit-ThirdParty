<template>
  <v-app>
    <v-app-bar app>
      <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->
      <router-link to="/">
        <v-img
          :src="require('@/assets/images/eq5d_logo.gif')"
          height="64"
          max-height="64"
          max-width="250"
        ></v-img>
      </router-link>
      <!-- <v-toolbar-title>EQ-5D</v-toolbar-title> -->
      <v-spacer></v-spacer>
      <v-btn icon to="/eq/question/setting">
        <v-icon>settings</v-icon>
      </v-btn>

      <!-- <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn> -->
    </v-app-bar>
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  })
};
</script>
