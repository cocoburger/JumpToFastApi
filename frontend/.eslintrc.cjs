module.exports = {
  extends: [
    'eslint:recommended'
  ],
  parserOptions: {
    ecmaVersion: 2020,
    sourceType: 'module',
    extraFileExtensions: [ '.svelte' ]
  },
  env: {
    es6: true,
    browser: true
  },
  overrides: [
    {
      files: [ '*.svelte' ],
      processor: 'svelte3/svelte3'
    }
  ],
  settings: {
    'svelte3/ignore-styles': () => true
  },
  plugins: [ 'svelte3' ],
  ignorePatterns: [ 'node_modules' ]
}