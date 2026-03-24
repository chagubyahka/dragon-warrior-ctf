(function () {
  const storageKey = "dragonCipher";

  if (!localStorage.getItem(storageKey)) {
    localStorage.setItem(
      storageKey,
      "7585dc573642c73b134a44fef52bb56e106c0da2d3d0be86275629ea182143ca"
    );
  }
  document.cookie = "user_pref=TGludDogQUVTICsgVVRGLTggbW9kZQ==; path=/";
})();