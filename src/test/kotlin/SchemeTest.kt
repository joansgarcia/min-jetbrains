import com.intellij.openapi.editor.colors.EditorColorsManager
import com.intellij.openapi.editor.colors.TextAttributesKey
import com.intellij.openapi.editor.colors.impl.EditorColorsSchemeImpl
import com.intellij.openapi.util.JDOMUtil
import com.intellij.testFramework.fixtures.BasePlatformTestCase
import java.io.File

/** Verifica que el esquema de editor resuelve los colores esperados sobre Darcula. */
class SchemeTest : BasePlatformTestCase() {
    fun testDarkSchemeResolvesKotlinColors() {
        val parent = EditorColorsManager.getInstance().allSchemes.first { it.name.contains("Darcula") }
        val scheme = EditorColorsSchemeImpl(parent)
        scheme.readExternal(JDOMUtil.load(File("src/main/resources/themes/min-dark.xml").toPath()))
        val expected = mapOf(
            "KOTLIN_KEYWORD" to 0xf97583, "KOTLIN_FUNCTION_CALL" to 0xb392f0,
            "KOTLIN_LOCAL_VARIABLE" to 0x79b8ff, "KOTLIN_PARAMETER" to 0xf8f8f8, "TEXT" to 0xcccccc,
        )
        for ((key, rgb) in expected) {
            val fg = scheme.getAttributes(TextAttributesKey.find(key))?.foregroundColor?.rgb?.and(0xffffff)
            assertEquals(key, rgb, fg)
        }
    }
}
