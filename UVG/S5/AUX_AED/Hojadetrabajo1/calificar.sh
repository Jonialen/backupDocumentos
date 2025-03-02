#!/bin/bash

PATH_AUX="$HOME/Documents/UVG/S5/AUX_AED/Hojadetrabajo1"
TAREAS_DIR="$PATH_AUX/pendientes"
REVISADAS_DIR="$PATH_AUX/revisadas"
TEMP_DIR="/tmp/tarea_actual"

# Asegurar limpieza
rm -rf "$TEMP_DIR"
mkdir -p "$TEMP_DIR"

compilar_codigo() {
    local DIR="$1"

    JAVA_FILES=$(find "$DIR" -name "*.java")
    if [ -z "$JAVA_FILES" ]; then
        echo "⚠️ No se encontraron archivos .java en $DIR"
        return
    fi

    echo "🔧 Compilando código en $DIR..."
    mkdir -p "$DIR/bin"
    javac $JAVA_FILES -d "$DIR/bin"
    if [ $? -ne 0 ]; then
        echo "❌ Error de compilación en $DIR"
    else
        echo "✅ Compilación exitosa en $DIR"
    fi
}

# 📌 Procesar archivo con links de GitHub
LINKS_FILE="$TAREAS_DIR/repos.txt"

if [ -f "$LINKS_FILE" ]; then
    echo "📄 Procesando repositorios desde: $LINKS_FILE"
    
    while read -r repo_link; do
        if [[ "$repo_link" =~ ^https://github.com/ ]]; then
            REPO_NAME=$(basename "$repo_link" .git)
            CLONE_DIR="$TEMP_DIR/$REPO_NAME"

            echo "🔄 Clonando $repo_link..."
            git clone --depth=1 "$repo_link" "$CLONE_DIR"

            compilar_codigo "$CLONE_DIR"
        fi
    done < "$LINKS_FILE"

    mv "$LINKS_FILE" "$REVISADAS_DIR/"
fi

# 📌 Procesar archivos ZIP
for archivo in "$TAREAS_DIR"/*.zip; do
    [ -e "$archivo" ] || continue

    echo "📂 Procesando ZIP: $archivo"
    unzip -q "$archivo" -d "$TEMP_DIR/zip"

    compilar_codigo "$TEMP_DIR/zip"
    mv "$archivo" "$REVISADAS_DIR/"
done

echo "🎉 Revisión completada."
