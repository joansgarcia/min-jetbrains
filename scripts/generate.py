#!/usr/bin/env python3
"""Genera src/main/resources/themes/{id}.theme.json y {id}.xml desde palettes/*.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "src/main/resources/themes"


def ui_theme(p, islands=False):
    c = p["colors"]
    t = {
        "name": ("Islands " if islands else "") + p["name"],
        "dark": p["dark"],
        "author": "sebastiandotdev (port of Min Theme by Miguel Solorio)",
        "editorScheme": f"/themes/{p['id']}.xml",
        "colors": {k: v for k, v in c.items()},
        "ui": {
            "*": {
                "foreground": "fg",
                "background": "bg",
                "selectionBackground": "selection",
                "selectionForeground": "fgStrong",
                "selectionInactiveBackground": "selection",
                "selectionInactiveForeground": "fgStrong",
                "disabledForeground": "fgDisabled",
                "disabledBackground": "bg",
                "inactiveForeground": "fgMuted",
                "separatorColor": "border",
                "borderColor": "border",
                "focusColor": "borderFocus",
                "infoForeground": "fgMuted",
                "acceleratorForeground": "fgMuted",
                "acceleratorSelectionForeground": "fgStrong",
            },
            "ActionButton": {"hoverBackground": "hover", "pressedBackground": "hover"},
            "Borders": {"color": "border", "ContrastBorderColor": "border"},
            "Button": {
                "background": "button",
                "foreground": "fgStrong",
                "startBackground": "button",
                "endBackground": "button",
                "startBorderColor": "button",
                "endBorderColor": "button",
                "focusedBorderColor": "borderFocus",
                "default": {
                    "foreground": "bg",
                    "startBackground": "fgStrong",
                    "endBackground": "fgStrong",
                    "startBorderColor": "fgStrong",
                    "endBorderColor": "fgStrong",
                    "focusedBorderColor": "borderFocus",
                },
            },
            "Component": {
                "borderColor": "border",
                "focusedBorderColor": "borderFocus",
                "focusColor": "borderFocus",
                "errorFocusColor": "red",
                "inactiveErrorFocusColor": "red",
                "warningFocusColor": "orange",
                "inactiveWarningFocusColor": "orange",
            },
            "CompletionPopup": {
                "background": "panel",
                "selectionBackground": "selectionFocus",
                "selectionInactiveBackground": "selection",
                "matchForeground": "fgStrong",
            },
            "Counter": {"background": "badge", "foreground": "badgeFg"},
            "DefaultTabs": {
                "background": "panel",
                "hoverBackground": "hover",
                "underlinedTabBackground": "bg",
                "underlineColor": "fgStrong",
                "inactiveUnderlineColor": "fgMuted",
                "underlineHeight": 1,
            },
            "EditorPane": {"background": "bg", "inactiveBackground": "bg"},
            "EditorTabs": {
                "background": "panel",
                "underlinedTabBackground": "bg",
                "underlinedTabForeground": "fgStrong",
                "underlineColor": "fgStrong",
                "inactiveUnderlineColor": "fgMuted",
                "hoverBackground": "hover",
                "borderColor": "panel",
                "inactiveColoredFileBackground": "panel",
                "underlineHeight": 1,
            },
            "Link": {"activeForeground": "fgStrong", "hoverForeground": "fgStrong",
                     "pressedForeground": "fgStrong", "visitedForeground": "fg",
                     "secondaryForeground": "fgMuted"},
            "List": {
                "background": "bg",
                "foreground": "fg",
                "hoverBackground": "hover",
                "hoverInactiveBackground": "hover",
                "selectionBackground": "selection",
                "selectionInactiveBackground": "selection",
                "selectionForeground": "fgStrong",
                "selectionInactiveForeground": "fgStrong",
            },
            "MainToolbar": {"background": "panel",
                            "Icon": {"background": "panel", "hoverBackground": "hover"}},
            "Menu": {"background": "panel", "foreground": "fg", "borderColor": "border",
                     "selectionBackground": "selection", "selectionForeground": "fgStrong"},
            "MenuBar": {"background": "panel", "selectionBackground": "selection"},
            "MenuItem": {"background": "panel", "foreground": "fg",
                         "selectionBackground": "selection", "selectionForeground": "fgStrong"},
            "NavBar": {"borderColor": "panel"},
            "Notification": {"background": "panel", "borderColor": "border",
                             "foreground": "fg", "errorBackground": "panel",
                             "errorBorderColor": "red", "errorForeground": "fg"},
            "OptionPane": {"background": "panel"},
            "Panel": {"background": "panel"},
            "ParameterInfo": {"background": "panel", "foreground": "fg", "borderColor": "border"},
            "Popup": {"Header": {"activeBackground": "panel", "inactiveBackground": "panel"},
                      "borderColor": "border", "inactiveBorderColor": "border",
                      "Toolbar": {"background": "panel", "borderColor": "border"}},
            "PopupMenu": {"background": "panel", "foreground": "fg",
                          "selectionBackground": "selection", "selectionForeground": "fgStrong"},
            "ProgressBar": {"foreground": "fgStrong", "trackColor": "border",
                            "progressColor": "fgStrong", "passedColor": "fgStrong",
                            "indeterminateStartColor": "fgStrong",
                            "indeterminateEndColor": "fgMuted"},
            "ScrollBar": {"thumbColor": "badge", "hoverThumbColor": "borderFocus",
                          "Thumb": {"background": "badge", "hoverBackground": "borderFocus"}},
            "SearchEverywhere": {"Header": {"background": "panelAlt"},
                                 "SearchField": {"background": "input", "borderColor": "border"}},
            "SearchMatch": {"startBackground": "textSelection", "endBackground": "textSelection"},
            "SidePanel": {"background": "panel"},
            "Separator": {"separatorColor": "border"},
            "SplitPane": {"background": "border"},
            "StatusBar": {"background": "panel", "borderColor": "panel", "foreground": "fg",
                          "hoverBackground": "hover"},
            "TabbedPane": {"background": "panel", "contrastColor": "border",
                           "focusColor": "selection", "hoverColor": "hover",
                           "underlineColor": "fgStrong", "selectedColor": "fgStrong",
                           "selectedBackground": "bg"},
            "Table": {"background": "bg", "foreground": "fg", "gridColor": "border",
                      "hoverBackground": "hover", "selectionBackground": "selection",
                      "selectionForeground": "fgStrong",
                      "selectionInactiveBackground": "selection",
                      "stripeColor": "panel"},
            "TableHeader": {"background": "panel", "borderColor": "border", "bottomSeparatorColor": "border"},
            "TextArea": {"background": "input", "foreground": "inputFg",
                         "selectionBackground": "textSelection", "selectionForeground": "fgStrong"},
            "TextField": {"background": "input", "foreground": "inputFg",
                          "borderColor": "border", "selectionBackground": "textSelection",
                          "selectionForeground": "fgStrong"},
            "ToggleButton": {"onBackground": "fgStrong", "offBackground": "badge",
                             "onForeground": "bg", "offForeground": "fg"},
            "ToolBar": {"background": "panel", "borderHandleColor": "fgDisabled",
                        "floatingForeground": "fg"},
            "ToolTip": {"background": "panelAlt", "foreground": "fgStrong",
                        "borderColor": "border", "infoForeground": "fgMuted"},
            "ToolWindow": {"Button": {"hoverBackground": "hover", "selectedBackground": "selection",
                                      "selectedForeground": "fgStrong"},
                           "Header": {"background": "panel", "inactiveBackground": "panel",
                                      "borderColor": "panel"}},
            "Tree": {"background": "panel", "foreground": "fg", "hash": "border",
                     "hoverBackground": "hover", "hoverInactiveBackground": "hover",
                     "selectionBackground": "selection", "selectionInactiveBackground": "selection",
                     "selectionForeground": "fgStrong", "selectionInactiveForeground": "fgStrong"},
            "VersionControl": {"FileHistory": {"Commit": {"selectedBranchBackground": "selection"}},
                               "Log": {"Commit": {"currentBranchBackground": "selection",
                                                  "hoveredBackground": "hover"}}},
            "WelcomeScreen": {"background": "bg", "borderColor": "border",
                              "captionBackground": "panel", "captionForeground": "fg",
                              "footerBackground": "panel", "footerForeground": "fgMuted",
                              "headerBackground": "bg", "headerForeground": "fgStrong",
                              "Projects": {"background": "panel", "selectionBackground": "selection",
                                           "selectionInactiveBackground": "selection"}},
        },
        "icons": {"ColorPalette": {}},
    }
    if islands:
        t["parentTheme"] = "Islands " + ("Dark" if p["dark"] else "Light")
        t["ui"]["Islands"] = 1
        t["ui"]["Island"] = {"borderColor": "panel"}
    return t


# ---- Editor color scheme -------------------------------------------------

def attr(name, fg=None, bg=None, font=None, effect=None, effect_type=None, base=None):
    if base:
        return f'    <option name="{name}" baseAttributes="{base}"/>'
    parts = []
    if fg:
        parts.append(f'        <option name="FOREGROUND" value="{fg[1:]}"/>')
    if bg:
        parts.append(f'        <option name="BACKGROUND" value="{bg[1:]}"/>')
    if font:
        parts.append(f'        <option name="FONT_TYPE" value="{font}"/>')
    if effect:
        parts.append(f'        <option name="EFFECT_COLOR" value="{effect[1:]}"/>')
        parts.append(f'        <option name="EFFECT_TYPE" value="{effect_type or 2}"/>')
    return f'    <option name="{name}">\n      <value>\n' + "\n".join(parts) + "\n      </value>\n    </option>"


def editor_scheme(p):
    c = p["colors"]
    d = p["dark"]
    colors = {
        "CARET_COLOR": c["caret"],
        "CARET_ROW_COLOR": c["lineHighlight"],
        "CONSOLE_BACKGROUND_KEY": c["bg"],
        "DIFF_SEPARATORS_BACKGROUND": c["panel"],
        "DOCUMENTATION_COLOR": c["panel"],
        "ERROR_HINT": c["diffDeleted"],
        "GUTTER_BACKGROUND": c["bg"],
        "INDENT_GUIDE": c["indentGuide"],
        "INFORMATION_HINT": c["panel"],
        "LINE_NUMBERS_COLOR": c["lineNumber"],
        "LINE_NUMBER_ON_CARET_ROW_COLOR": c["fgStrong"],
        "METHOD_SEPARATORS_COLOR": c["border"],
        "MODIFIED_LINES_COLOR": c["blue"],
        "ADDED_LINES_COLOR": c["green"],
        "DELETED_LINES_COLOR": c["red"],
        "RECURSIVE_CALL_ATTRIBUTES": c["bg"],
        "RIGHT_MARGIN_COLOR": c["indentGuide"],
        "SELECTED_INDENT_GUIDE": c["indentGuideActive"],
        "SELECTION_BACKGROUND": c["textSelection"],
        "SELECTION_FOREGROUND": c["fgStrong"],
        "SOFT_WRAP_SIGN_COLOR": c["lineNumber"],
        "TEARLINE_COLOR": c["border"],
        "WHITESPACES_COLOR": c["indentGuide"],
        "ANNOTATIONS_COLOR": c["fg"],
        "READONLY_FRAGMENT_BACKGROUND": c["panel"],
        "VISUAL_INDENT_GUIDE": c["indentGuide"],
    }
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           f'<scheme name="{p["name"]}" version="142" parent_scheme="{"Darcula" if d else "Default"}">',
           "  <colors>"]
    out += [f'    <option name="{k}" value="{v[1:]}"/>' for k, v in sorted(colors.items())]
    out += ["  </colors>", "  <attributes>"]

    A = []
    # --- core (DEFAULT_*) ---
    A += [
        attr("TEXT", fg=c["text"], bg=c["bg"]),
        attr("DEFAULT_ATTRIBUTE", fg=c["attribute"]),
        attr("DEFAULT_BLOCK_COMMENT", fg=c["comment"]),
        attr("DEFAULT_BRACES", fg=c["punctuation"]),
        attr("DEFAULT_BRACKETS", fg=c["punctuation"]),
        attr("DEFAULT_CLASS_NAME", fg=c["type"]),
        attr("DEFAULT_CLASS_REFERENCE", fg=c["type"]),
        attr("DEFAULT_COMMA", fg=c["punctuation"]),
        attr("DEFAULT_CONSTANT", fg=c["constant"]),
        attr("DEFAULT_DOC_COMMENT", fg=c["comment"]),
        attr("DEFAULT_DOC_COMMENT_TAG", fg=c["comment"], font=1),
        attr("DEFAULT_DOC_COMMENT_TAG_VALUE", fg=c["comment"]),
        attr("DEFAULT_DOC_MARKUP", fg=c["comment"]),
        attr("DEFAULT_ENTITY", fg=c["constant"]),
        attr("DEFAULT_FUNCTION_CALL", fg=c["function"]),
        attr("DEFAULT_FUNCTION_DECLARATION", fg=c["function"]),
        attr("DEFAULT_GLOBAL_VARIABLE", fg=c["constant"]),
        attr("DEFAULT_CLASS_NAME", fg=c["type"]),
        attr("DEFAULT_IDENTIFIER", fg=c["text"]),
        attr("DEFAULT_INSTANCE_FIELD", fg=c["text"]),
        attr("DEFAULT_INSTANCE_METHOD", fg=c["function"]),
        attr("DEFAULT_INTERFACE_NAME", fg=c["type"]),
        attr("DEFAULT_INVALID_STRING_ESCAPE", fg=c["red"], effect=c["red"], effect_type=2),
        attr("DEFAULT_KEYWORD", fg=c["keyword"]),
        attr("DEFAULT_LABEL", fg=c["constant"]),
        attr("DEFAULT_LINE_COMMENT", fg=c["comment"]),
        attr("DEFAULT_LOCAL_VARIABLE", fg=c["constant"]),
        attr("DEFAULT_METADATA", fg=c["keyword"]),
        attr("DEFAULT_NUMBER", fg=c["number"]),
        attr("DEFAULT_OPERATION_SIGN", fg=c["keyword"]),
        attr("DEFAULT_PARAMETER", fg=c["parameter"]),
        attr("DEFAULT_PARENTHS", fg=c["punctuation"]),
        attr("DEFAULT_PREDEFINED_SYMBOL", fg=c["constant"]),
        attr("DEFAULT_SEMICOLON", fg=c["punctuation"]),
        attr("DEFAULT_STATIC_FIELD", fg=c["constant"], font=2),
        attr("DEFAULT_STATIC_METHOD", fg=c["function"], font=2),
        attr("DEFAULT_STRING", fg=c["string"]),
        attr("DEFAULT_TAG", fg=c["tag"]),
        attr("DEFAULT_TEMPLATE_LANGUAGE_COLOR", fg=c["text"]),
        attr("DEFAULT_VALID_STRING_ESCAPE", fg=c["constant"]),
        attr("DEFAULT_DOT", fg=c["punctuation"]),
    ]
    # --- code semantics ---
    A += [
        attr("CLASS_NAME_ATTRIBUTES", fg=c["type"]),
        attr("CONSTRUCTOR_CALL_ATTRIBUTES", base="DEFAULT_FUNCTION_CALL"),
        attr("CONSTRUCTOR_DECLARATION_ATTRIBUTES", base="DEFAULT_FUNCTION_DECLARATION"),
        attr("ENUM_CONST", fg=c["constant"]),
        attr("INTERFACE_NAME_ATTRIBUTES", base="DEFAULT_INTERFACE_NAME"),
        attr("ANNOTATION_NAME_ATTRIBUTES", fg=c["keyword"]),
        attr("ANNOTATION_ATTRIBUTE_NAME_ATTRIBUTES", fg=c["attribute"]),
        attr("METHOD_CALL_ATTRIBUTES", base="DEFAULT_FUNCTION_CALL"),
        attr("METHOD_DECLARATION_ATTRIBUTES", base="DEFAULT_FUNCTION_DECLARATION"),
        attr("PARAMETER_ATTRIBUTES", base="DEFAULT_PARAMETER"),
        attr("LOCAL_VARIABLE_ATTRIBUTES", base="DEFAULT_LOCAL_VARIABLE"),
        attr("INSTANCE_FIELD_ATTRIBUTES", base="DEFAULT_INSTANCE_FIELD"),
        attr("STATIC_FIELD_ATTRIBUTES", base="DEFAULT_STATIC_FIELD"),
        attr("STATIC_METHOD_ATTRIBUTES", base="DEFAULT_STATIC_METHOD"),
        attr("TYPE_PARAMETER_NAME_ATTRIBUTES", fg=c["type"]),
        attr("KOTLIN_NAMED_ARGUMENT", fg=c["parameter"]),
        attr("KOTLIN_SMART_CAST_VALUE", bg=c["lineHighlight"]),
        attr("KOTLIN_MUTABLE_VARIABLE", fg=c["constant"]),
        attr("KOTLIN_VARIABLE_AS_FUNCTION", fg=c["function"]),
        attr("KOTLIN_VARIABLE_AS_FUNCTION_LIKE", fg=c["function"]),
        attr("KOTLIN_EXCLEXCL", fg=c["keyword"]),
        attr("KOTLIN_QUEST", fg=c["keyword"]),
        attr("KOTLIN_LABEL", fg=c["constant"]),
        attr("KOTLIN_TYPE_PARAMETER", fg=c["type"]),
        attr("KOTLIN_ENUM_ENTRY", fg=c["constant"]),
        attr("JS.LOCAL_VARIABLE", base="DEFAULT_LOCAL_VARIABLE"),
        attr("JS.PARAMETER", base="DEFAULT_PARAMETER"),
        attr("JS.GLOBAL_VARIABLE", base="DEFAULT_GLOBAL_VARIABLE"),
        attr("JS.GLOBAL_FUNCTION", base="DEFAULT_FUNCTION_DECLARATION"),
        attr("JS.INSTANCE_MEMBER_FUNCTION", base="DEFAULT_INSTANCE_METHOD"),
        attr("JS.DECORATOR", fg=c["keyword"]),
        attr("JS.REGEXP", fg=c["string"]),
        attr("TS.MODULE_NAME", fg=c["text"]),
        attr("TS.TYPE_PARAMETER", fg=c["type"]),
        attr("JAVA_KEYWORD", base="DEFAULT_KEYWORD"),
        attr("JAVA_STRING", base="DEFAULT_STRING"),
        attr("JAVA_NUMBER", base="DEFAULT_NUMBER"),
        attr("JAVA_LINE_COMMENT", base="DEFAULT_LINE_COMMENT"),
        attr("JAVA_BLOCK_COMMENT", base="DEFAULT_BLOCK_COMMENT"),
        attr("JAVA_DOC_COMMENT", base="DEFAULT_DOC_COMMENT"),
        attr("JAVA_DOC_TAG", base="DEFAULT_DOC_COMMENT_TAG"),
        attr("JAVA_BRACES", base="DEFAULT_BRACES"),
        attr("JAVA_BRACKETS", base="DEFAULT_BRACKETS"),
        attr("JAVA_PARENTH", base="DEFAULT_PARENTHS"),
        attr("JAVA_OPERATION_SIGN", base="DEFAULT_OPERATION_SIGN"),
        attr("JAVA_COMMA", base="DEFAULT_COMMA"),
        attr("JAVA_DOT", base="DEFAULT_DOT"),
        attr("JAVA_SEMICOLON", base="DEFAULT_SEMICOLON"),
        attr("JAVA_VALID_STRING_ESCAPE", base="DEFAULT_VALID_STRING_ESCAPE"),
        attr("JAVA_INVALID_STRING_ESCAPE", base="DEFAULT_INVALID_STRING_ESCAPE"),
        attr("KOTLIN_FUNCTION_LITERAL_BRACES_AND_ARROW", base="DEFAULT_BRACES"),
        attr("KOTLIN_PACKAGE_FUNCTION_CALL", base="DEFAULT_FUNCTION_CALL"),
        attr("KOTLIN_CONSTRUCTOR", base="DEFAULT_FUNCTION_CALL"),
    ]
    # --- Kotlin: keys explícitas (el esquema padre Darcula las pisa si no) ---
    kt = {}
    for k in ["KEYWORD", "KEYWORD_VAL", "KEYWORD_VAR", "OPERATION_SIGN", "ARROW", "SAFE_ACCESS",
              "EXCLEXCL", "QUEST", "DOUBLE_COLON"]:
        kt[k] = dict(fg=c["keyword"])
    for k in ["CLASS", "ABSTRACT_CLASS", "DATA_CLASS", "DATA_OBJECT", "TRAIT", "OBJECT", "ENUM",
              "TYPE_ALIAS", "TYPE_PARAMETER", "CONSTRUCTOR"]:
        kt[k] = dict(fg=c["type"])
    for k in ["FUNCTION_CALL", "FUNCTION_DECLARATION", "EXTENSION_FUNCTION_CALL",
              "PACKAGE_FUNCTION_CALL", "SUSPEND_FUNCTION_CALL", "DYNAMIC_FUNCTION_CALL",
              "VARIABLE_AS_FUNCTION", "VARIABLE_AS_FUNCTION_LIKE"]:
        kt[k] = dict(fg=c["function"])
    for k in ["LOCAL_VARIABLE", "MUTABLE_VARIABLE", "CLOSURE_DEFAULT_PARAMETER", "ENUM_ENTRY",
              "LABEL", "SMART_CONSTANT"]:
        kt[k] = dict(fg=c["constant"])
    for k in ["INSTANCE_PROPERTY", "INSTANCE_PROPERTY_CUSTOM_PROPERTY_DECLARATION",
              "PACKAGE_PROPERTY", "PACKAGE_PROPERTY_CUSTOM_PROPERTY_DECLARATION",
              "EXTENSION_PROPERTY", "SYNTHETIC_EXTENSION_PROPERTY", "DYNAMIC_PROPERTY_CALL",
              "BACKING_FIELD_VARIABLE"]:
        kt[k] = dict(fg=c["string2"])
    kt["NAMED_ARGUMENT"] = dict(fg=c["parameter"])
    for k in ["PARAMETER", "ANNOTATION_ATTRIBUTE_NAME_ATTRIBUTES"]:
        kt[k] = dict(fg=c["parameter"])
    kt["ANNOTATION"] = dict(fg=c["keyword"])
    kt["BUILTIN_ANNOTATION"] = dict(fg=c["keyword"])  # modificadores: private, const, override...
    kt["STRING"] = dict(fg=c["string"])
    kt["STRING_ESCAPE"] = dict(fg=c["constant"])
    kt["INVALID_STRING_ESCAPE"] = dict(fg=c["red"], effect=c["red"], effect_type=2)
    kt["NUMBER"] = dict(fg=c["number"])
    kt["LINE_COMMENT"] = kt["BLOCK_COMMENT"] = kt["DOC_COMMENT"] = dict(fg=c["comment"])
    for k in ["BRACES", "BRACKETS", "PARENTHESIS", "COMMA", "DOT", "SEMICOLON", "COLON"]:
        kt[k] = dict(fg=c["punctuation"])
    for k, v in kt.items():
        A.append(attr("KOTLIN_" + k, **v))
    # --- markup: html / xml / css / json / yaml / markdown ---
    A += [
        attr("HTML_TAG", base="DEFAULT_TAG"),
        attr("HTML_TAG_NAME", fg=c["tag"]),
        attr("HTML_ATTRIBUTE_NAME", fg=c["attribute"]),
        attr("HTML_ATTRIBUTE_VALUE", base="DEFAULT_STRING"),
        attr("HTML_ENTITY_REFERENCE", base="DEFAULT_ENTITY"),
        attr("HTML_COLOR", base="DEFAULT_STRING"),
        attr("HTML_CODE", fg=c["text"]),
        attr("XML_TAG", base="DEFAULT_TAG"),
        attr("XML_TAG_NAME", fg=c["tag"]),
        attr("XML_TAG_DATA", fg=c["text"]),
        attr("XML_ATTRIBUTE_NAME", fg=c["attribute"]),
        attr("XML_ATTRIBUTE_VALUE", base="DEFAULT_STRING"),
        attr("XML_ENTITY_REFERENCE", base="DEFAULT_ENTITY"),
        attr("XML_PROLOGUE", fg=c["comment"]),
        attr("XML_TAG_NAME", fg=c["tag"]),
        attr("CSS.PROPERTY_NAME", fg=c["constant"]),
        attr("CSS.PROPERTY_VALUE", fg=c["number"]),
        attr("CSS.TAG_NAME", fg=c["tag"]),
        attr("CSS.CLASS_NAME", fg=c["type"]),
        attr("CSS.IDENT", fg=c["text"]),
        attr("CSS.FUNCTION", base="DEFAULT_FUNCTION_CALL"),
        attr("CSS.COLOR", fg=c["number"]),
        attr("CSS.NUMBER", fg=c["number"]),
        attr("CSS.STRING", base="DEFAULT_STRING"),
        attr("CSS.URL", fg=c["string"]),
        attr("CSS.KEYWORD", base="DEFAULT_KEYWORD"),
        attr("CSS.COMMENT", base="DEFAULT_BLOCK_COMMENT"),
        attr("CSS.ATTRIBUTE_NAME", fg=c["attribute"]),
        attr("CSS.PSEUDO", fg=c["keyword"]),
        attr("CSS.IMPORTANT", fg=c["keyword"]),
        attr("CSS.BRACES", base="DEFAULT_BRACES"),
        attr("CSS.PARENTHESES", base="DEFAULT_PARENTHS"),
        attr("CSS.COMMA", base="DEFAULT_COMMA"),
        attr("CSS.SEMICOLON", base="DEFAULT_SEMICOLON"),
        attr("JSON.PROPERTY_KEY", fg=c["number"] if d else c["keyword"]),
        attr("JSON.STRING", base="DEFAULT_STRING"),
        attr("JSON.NUMBER", base="DEFAULT_NUMBER"),
        attr("JSON.KEYWORD", fg=c["constant"]),
        attr("JSON.BRACES", base="DEFAULT_BRACES"),
        attr("JSON.BRACKETS", base="DEFAULT_BRACKETS"),
        attr("JSON.COMMA", base="DEFAULT_COMMA"),
        attr("JSON.COLON", fg=c["keyword"]),
        attr("JSON.PARAMETER", fg=c["parameter"]),
        attr("JSON.LINE_COMMENT", base="DEFAULT_LINE_COMMENT"),
        attr("JSON.BLOCK_COMMENT", base="DEFAULT_BLOCK_COMMENT"),
        attr("YAML_SCALAR_KEY", fg=c["number"] if d else c["keyword"]),
        attr("YAML_SCALAR_VALUE", base="DEFAULT_STRING"),
        attr("YAML_SCALAR_STRING", base="DEFAULT_STRING"),
        attr("YAML_SCALAR_DSTRING", base="DEFAULT_STRING"),
        attr("YAML_SCALAR_LIST", base="DEFAULT_STRING"),
        attr("YAML_COMMENT", base="DEFAULT_LINE_COMMENT"),
        attr("YAML_SIGN", fg=c["keyword"]),
        attr("YAML_ANCHOR", fg=c["parameter"]),
        attr("YAML_TEXT", fg=c["text"]),
        attr("TOML_KEY", fg=c["number"] if d else c["keyword"]),
        attr("TOML_STRING", base="DEFAULT_STRING"),
        attr("TOML_NUMBER", base="DEFAULT_NUMBER"),
        attr("TOML_COMMENT", base="DEFAULT_LINE_COMMENT"),
        attr("TOML_BOOLEAN", fg=c["constant"]),
        attr("TOML_TABLE", fg=c["function"]),
        attr("MARKDOWN_HEADER_LEVEL_1", fg=c["red"] if d else c["function"], font=1),
        attr("MARKDOWN_HEADER_LEVEL_2", fg=c["red"] if d else c["function"], font=1),
        attr("MARKDOWN_HEADER_LEVEL_3", fg=c["red"] if d else c["function"], font=1),
        attr("MARKDOWN_HEADER_LEVEL_4", fg=c["red"] if d else c["function"], font=1),
        attr("MARKDOWN_HEADER_LEVEL_5", fg=c["red"] if d else c["function"], font=1),
        attr("MARKDOWN_HEADER_LEVEL_6", fg=c["red"] if d else c["function"], font=1),
        attr("MARKDOWN_BOLD", fg=c["red"] if d else c["function"], font=1),
        attr("MARKDOWN_ITALIC", font=2),
        attr("MARKDOWN_BOLD_ITALIC", font=3),
        attr("MARKDOWN_LIST_MARKER", fg=c["red"] if d else c["function"]),
        attr("MARKDOWN_LINK_DESTINATION", fg=c["string"]),
        attr("MARKDOWN_LINK_TEXT", fg=c["constant"]),
        attr("MARKDOWN_CODE_SPAN", fg=c["string2"]),
        attr("MARKDOWN_CODE_BLOCK", fg=c["string2"]),
        attr("MARKDOWN_BLOCK_QUOTE", fg=c["comment"]),
        attr("MARKDOWN_EXPLICIT_LINK", fg=c["string"], effect=c["string"], effect_type=1),
    ]
    # --- editor chrome / inspections / search / VCS ---
    A += [
        attr("BREAKPOINT_ATTRIBUTES", bg=c["diffDeleted"]),
        attr("BAD_CHARACTER", fg=c["red"], effect=c["red"], effect_type=2),
        attr("CTRL_CLICKABLE", fg=c["fgStrong"], effect=c["fgStrong"], effect_type=1),
        attr("DEPRECATED_ATTRIBUTES", effect=c["fgMuted"], effect_type=3),
        attr("ERRORS_ATTRIBUTES", effect=c["red"], effect_type=2),
        attr("WARNING_ATTRIBUTES", effect=c["orange"], effect_type=2),
        attr("WEAK_WARNING_ATTRIBUTES", effect=c["fgMuted"], effect_type=2),
        attr("INFO_ATTRIBUTES", effect=c["blue"], effect_type=2),
        attr("NOT_USED_ELEMENT_ATTRIBUTES", fg=c["fgMuted"]),
        attr("WRONG_REFERENCES_ATTRIBUTES", fg=c["red"]),
        attr("RUNTIME_ERROR", effect=c["red"], effect_type=2),
        attr("EXECUTIONPOINT_ATTRIBUTES", bg=c["diffModified"]),
        attr("IDENTIFIER_UNDER_CARET_ATTRIBUTES", bg=c["textSelection"]),
        attr("WRITE_IDENTIFIER_UNDER_CARET_ATTRIBUTES", bg=c["textSelection"]),
        attr("MATCHED_BRACE_ATTRIBUTES", bg=c["textSelection"], font=1),
        attr("UNMATCHED_BRACE_ATTRIBUTES", bg=c["diffDeleted"]),
        attr("SEARCH_RESULT_ATTRIBUTES", bg=c["diffModified"]),
        attr("TEXT_SEARCH_RESULT_ATTRIBUTES", bg=c["diffModified"]),
        attr("FOLDED_TEXT_ATTRIBUTES", fg=c["fgMuted"], bg=c["panel"]),
        attr("TODO_DEFAULT_ATTRIBUTES", fg=c["blue"], font=3),
        attr("HYPERLINK_ATTRIBUTES", fg=c["fgStrong"], effect=c["fgStrong"], effect_type=1),
        attr("FOLLOWED_HYPERLINK_ATTRIBUTES", fg=c["fg"], effect=c["fg"], effect_type=1),
        attr("INLAY_DEFAULT", fg=c["fgMuted"], bg=c["panel"]),
        attr("INLINE_PARAMETER_HINT", fg=c["fgMuted"], bg=c["panel"]),
        attr("INLINE_PARAMETER_HINT_CURRENT", fg=c["fgStrong"], bg=c["textSelection"]),
        attr("INLINE_PARAMETER_HINT_HIGHLIGHTED", fg=c["fgStrong"], bg=c["textSelection"]),
        attr("LIVE_TEMPLATE_ATTRIBUTES", bg=c["panel"]),
        attr("TEMPLATE_VARIABLE_ATTRIBUTES", fg=c["parameter"]),
        attr("LOOKUP_ELEMENT_ATTRIBUTES", fg=c["fg"]),
        attr("LINE_FULL_COVERAGE", fg=c["green"]),
    ]
    # --- console / terminal ANSI ---
    ansi = {
        "BLACK": c["ansiBlack"], "RED": c["ansiRed"], "GREEN": c["ansiGreen"],
        "YELLOW": c["ansiYellow"], "BLUE": c["ansiBlue"], "MAGENTA": c["ansiMagenta"],
        "CYAN": c["ansiCyan"], "WHITE": c["ansiWhite"],
    }
    for n, v in ansi.items():
        A.append(attr(f"CONSOLE_{n}_OUTPUT", fg=v))
    A += [
        attr("CONSOLE_DARKGRAY_OUTPUT", fg=c["ansiBrightBlack"]),
        attr("CONSOLE_GRAY_OUTPUT", fg=c["ansiWhite"]),
        attr("CONSOLE_NORMAL_OUTPUT", fg=c["text"] if not d else c["punctuation"]),
        attr("CONSOLE_ERROR_OUTPUT", fg=c["red"]),
        attr("CONSOLE_SYSTEM_OUTPUT", fg=c["fg"]),
        attr("CONSOLE_USER_INPUT", fg=c["string"]),
        attr("LOG_ERROR_OUTPUT", fg=c["red"]),
        attr("LOG_WARNING_OUTPUT", fg=c["orange"]),
        attr("LOG_INFO_OUTPUT", fg=c["blue"]),
        attr("LOG_DEBUG_OUTPUT", fg=c["fgMuted"]),
        attr("LOG_VERBOSE_OUTPUT", fg=c["fgMuted"]),
        attr("LOG_EXPIRED_ENTRY", fg=c["fgMuted"]),
    ]
    # dedupe by name, keep last definition
    seen = {}
    for a in A:
        name = a.split('"', 2)[1]
        seen[name] = a
    out += [seen[k] for k in sorted(seen)]
    out += ["  </attributes>", "</scheme>", ""]
    return "\n".join(out)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for f in sorted((ROOT / "palettes").glob("*.json")):
        p = json.loads(f.read_text())
        (OUT / f"{p['id']}.theme.json").write_text(json.dumps(ui_theme(p), indent=2) + "\n")
        (OUT / f"{p['id']}-islands.theme.json").write_text(json.dumps(ui_theme(p, True), indent=2) + "\n")
        (OUT / f"{p['id']}.xml").write_text(editor_scheme(p))
        print("generated", p["id"])


if __name__ == "__main__":
    main()
