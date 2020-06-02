<template>
  <div class="about">
    <h1>This is an about page</h1>
    {{ disTime }} -- {{ disFormatTime }}
  </div>
</template>

<script>
var intervalTimer;
export default {
  data() {
    return {
      disTime: 0,
      disFormatTime: "00:00:00",
    };
  },
  mounted() {
    this.countTime();
  },
  beforeDestroy() {
    clearInterval(intervalTimer);
  },
  methods: {
    countTime() {
      intervalTimer = setInterval(() => {
        this.disTime = this.disTime + 1;
        this.disFormatTime = this.displayTime(this.disTime);
      }, 1000);
    },
    displayTime(time) {
      const hours = Math.floor(time / 3600);
      const minutes = Math.floor(time / 60);
      const seconds = time % 60;

      return `${this.zeroPadded(hours)}:${this.zeroPadded(
        minutes
      )}:${this.zeroPadded(seconds)}`;
    },
    zeroPadded(num) {
      // 4 --> 04
      return num < 10 ? `0${num}` : num;
    },
  },
};
</script>
