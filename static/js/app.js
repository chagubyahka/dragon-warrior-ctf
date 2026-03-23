(function () {
  const storageKey = "dragonCipher";

  if (!localStorage.getItem(storageKey)) {
    localStorage.setItem(
      storageKey,
      "PUT_YOUR_CIPHERTEXT_HERE"
    );
  }
})();