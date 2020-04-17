var app = new Vue({
    el: "#app",
    data: {
      c100: 0,
      rc100: 0,
      c50: 0,
      rc50: 0,
      c20: 0,
      rc20: 0,
      c10: 0,
      rc10: 0,
      c5: 0,
      rc5: 0,
      c2: 0,
      rc2: 0,
      m1: 0,
      rm1: 0,
      m050: 0,
      rm050: 0,
      m025: 0,
      rm025: 0,
      m010: 0,
      rm010: 0,
      m05: 0,
      rm05: 0
    },
    watch: {
      c100: function() {
        this.rc100 = this.c100 * 100;
      },
      c50: function() {
        this.rc50 = this.c50 * 50;
      },
      c20: function() {
        this.rc20 = this.c20 * 20;
      },
      c10: function() {
        this.rc10 = this.c10 * 10;
      },
      c5: function() {
        this.rc5 = this.c5 * 5;
      },
      c2: function() {
        this.rc2 = this.c2 * 2;
      },
      m1: function() {
        this.rm1 = this.m1 * 1;
      },
      m050: function() {
        this.rm050 = this.m050 * 0.5;
      },
      m025: function() {
        this.rm025 = this.m025 * 0.25;
      },
      m010: function() {
        this.rm010 = this.m010 * 0.1;
      },
      m05: function() {
        this.rm05 = this.m05 * 0.05;
      }
    },
    computed: {
      soma: function() {
        return (
          this.rc100 +
          this.rc50 +
          this.rc20 +
          this.rc10 +
          this.rc5 +
          this.rc2 +
          this.rm1 +
          this.rm050 +
          this.rm025 +
          this.rm010 +
          this.rm05
        );
      }
    }
  });