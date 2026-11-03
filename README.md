# Min Theme for JetBrains

Port of [Min Theme](https://github.com/miguelsolorio/min-theme) (Miguel Solorio) to JetBrains IDEs.
Variants: **Min Dark**, **Min Light**.

## Structure

```
palettes/                  # source of truth: colors per variant (from the VS Code theme)
scripts/generate.py        # palettes -> src/main/resources/themes/*.theme.json + *.xml
src/main/resources/
  META-INF/plugin.xml      # themeProvider + bundledColorScheme
  themes/                  # generated UI theme + editor color scheme
.run/                      # IDE run configurations
```

## Development

```sh
python3 scripts/generate.py   # regenerate themes after editing palettes/
./gradlew runIde              # try it in a sandbox IDE
./gradlew buildPlugin         # build/distributions/*.zip
```

Requires JDK 21.

## License

MIT. Original theme © Miguel Solorio.
