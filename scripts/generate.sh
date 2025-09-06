#!/bin/bash

# Generates EVE ESI client using `openapi-generator-cli` with configurable options.

set -e  # Exit on any error

# Default values
OUTPUT_DIR="."
INPUT_SPEC="openapi.json"
GENERATOR="python"
PACKAGE_NAME="eve_esi_python"
PACKAGE_VERSION="0.1.0"
PROJECT_NAME="eve-esi-python"
API_NAME_SUFFIX=""
GIT_HOST="github.com"
GIT_REPO_ID="eve-esi-python"
GIT_USER_ID="puffingprie"
HTTP_USER_AGENT="eve-esi-client/0.1.0/python"
TEMPLATE_DIR=".openapi-generator-template/python"
CONFIG_FILE=""
LIBRARY=""
ADDITIONAL_PROPS=""
SKIP_OVERWRITE=false
ENABLE_POST_PROCESS=false
DRY_RUN=false
VERBOSE=false
FORCE_DOWNLOAD=false

# Function to display usage
show_usage() {
    cat << EOF
Usage: $0 [OPTIONS]

Generates EVE ESI Python client using openapi-generator-cli.

COMMON OPTIONS:
    -i, --input-spec FILE       Input OpenAPI spec file or URL (default: $INPUT_SPEC)
    -o, --output DIR            Output directory (default: $OUTPUT_DIR)
    -g, --generator-name TYPE   Generator type (default: $GENERATOR)
    -c, --config FILE           Configuration file (JSON or YAML)
    -t, --template-dir DIR      Custom template directory
    --package-name NAME         Package name (default: $PACKAGE_NAME)
    --library LIBRARY           Library template/sub-template
    --force-download            Force download latest OpenAPI spec from ESI

NAMING OPTIONS:
    --api-name-suffix SUFFIX    API name suffix (default: $API_NAME_SUFFIX)
    --model-name-prefix PREFIX  Prefix for all model names
    --model-name-suffix SUFFIX  Suffix for all model names
    --api-package PACKAGE       Package for generated API classes
    --model-package PACKAGE     Package for generated model classes
    --invoker-package PACKAGE   Root package for generated code

GIT/PROJECT OPTIONS:
    --git-host HOST             Git host (default: $GIT_HOST)
    --git-repo-id REPO          Git repository ID (default: $GIT_REPO_ID)
    --git-user-id USER          Git user ID (default: $GIT_USER_ID)
    --http-user-agent AGENT     HTTP user agent (default: $HTTP_USER_AGENT)

GENERATION OPTIONS:
    -p, --additional-properties PROPS  Additional properties (format: key1=value1,key2=value2)
    -s, --skip-overwrite        Skip overwriting existing files
    --enable-post-process-file  Enable post-processing using environment variables
    --dry-run                   Preview changes without making them
    --minimal-update            Only write files that have changed
    -v, --verbose               Enable verbose output

EXAMPLES:
    # Basic usage with custom output
    $0 -o ./my-client

    # Use custom package and version
    $0 --package-name my_esi_client -p packageVersion=2.0.0

    # Use configuration file
    $0 -c config.yaml -o ./configured-client

    # Force download and dry run
    $0 --force-download --dry-run

    # Custom template and library
    $0 -t ./templates --library asyncio

    # Multiple options combined
    $0 -o ./client --package-name custom_esi -p "packageVersion=2.0.0,generateSourceCodeOnly=true"

FLAGS:
    -h, --help                  Show this help message

For more information about openapi-generator-cli options, visit:
https://openapi-generator.tech/docs/usage

EOF
}

# Parse command line arguments
while [ $# -gt 0 ]; do
    case $1 in
        -i|--input-spec)
            INPUT_SPEC="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        -g|--generator-name)
            GENERATOR="$2"
            shift 2
            ;;
        -c|--config)
            CONFIG_FILE="$2"
            shift 2
            ;;
        -t|--template-dir)
            TEMPLATE_DIR="$2"
            shift 2
            ;;
        --package-name)
            PACKAGE_NAME="$2"
            shift 2
            ;;
        --library)
            LIBRARY="$2"
            shift 2
            ;;
        --api-name-suffix)
            API_NAME_SUFFIX="$2"
            shift 2
            ;;
        --model-name-prefix)
            MODEL_NAME_PREFIX="$2"
            shift 2
            ;;
        --model-name-suffix)
            MODEL_NAME_SUFFIX="$2"
            shift 2
            ;;
        --api-package)
            API_PACKAGE="$2"
            shift 2
            ;;
        --model-package)
            MODEL_PACKAGE="$2"
            shift 2
            ;;
        --invoker-package)
            INVOKER_PACKAGE="$2"
            shift 2
            ;;
        --git-host)
            GIT_HOST="$2"
            shift 2
            ;;
        --git-repo-id)
            GIT_REPO_ID="$2"
            shift 2
            ;;
        --git-user-id)
            GIT_USER_ID="$2"
            shift 2
            ;;
        --http-user-agent)
            HTTP_USER_AGENT="$2"
            shift 2
            ;;
        -p|--additional-properties)
            ADDITIONAL_PROPS="$2"
            shift 2
            ;;
        -s|--skip-overwrite)
            SKIP_OVERWRITE=true
            shift
            ;;
        --enable-post-process-file)
            ENABLE_POST_PROCESS=true
            shift
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --minimal-update)
            MINIMAL_UPDATE=true
            shift
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        --force-download)
            FORCE_DOWNLOAD=true
            shift
            ;;
        -h|--help)
            show_usage
            exit 0
            ;;
        *)
            echo "❌ Unknown option: $1"
            echo "Use -h or --help for usage information."
            exit 1
            ;;
    esac
done

echo "🚀 Generating EVE ESI Python client..."
echo "📂 Output directory: $OUTPUT_DIR"
echo "📦 Package name: $PACKAGE_NAME"
echo "🏷️  Generator: $GENERATOR"

# Download latest ESI OpenAPI spec if needed
if [ "$INPUT_SPEC" = "openapi.json" ] && { [ ! -f "$INPUT_SPEC" ] || [ "$FORCE_DOWNLOAD" = true ]; }; then
    echo "📥 Downloading latest ESI OpenAPI spec..."
    curl -o "$INPUT_SPEC" https://esi.evetech.net/meta/openapi.json
else
    echo "📄 Using input spec: $INPUT_SPEC"
fi

echo "⚙️ Generating client code..."

# Build the command
CMD="uv run openapi-generator-cli generate"
CMD="$CMD -i \"$INPUT_SPEC\""
CMD="$CMD -g \"$GENERATOR\""
CMD="$CMD -o \"$OUTPUT_DIR\""

# Add optional parameters
[ -n "$CONFIG_FILE" ] && CMD="$CMD -c \"$CONFIG_FILE\""
[ -n "$TEMPLATE_DIR" ] && CMD="$CMD -t \"$TEMPLATE_DIR\""
[ -n "$LIBRARY" ] && CMD="$CMD --library \"$LIBRARY\""
[ -n "$API_NAME_SUFFIX" ] && CMD="$CMD --api-name-suffix \"$API_NAME_SUFFIX\""
[ -n "$MODEL_NAME_PREFIX" ] && CMD="$CMD --model-name-prefix \"$MODEL_NAME_PREFIX\""
[ -n "$MODEL_NAME_SUFFIX" ] && CMD="$CMD --model-name-suffix \"$MODEL_NAME_SUFFIX\""
[ -n "$API_PACKAGE" ] && CMD="$CMD --api-package \"$API_PACKAGE\""
[ -n "$MODEL_PACKAGE" ] && CMD="$CMD --model-package \"$MODEL_PACKAGE\""
[ -n "$INVOKER_PACKAGE" ] && CMD="$CMD --invoker-package \"$INVOKER_PACKAGE\""
[ -n "$PACKAGE_NAME" ] && CMD="$CMD --package-name \"$PACKAGE_NAME\""
[ -n "$GIT_HOST" ] && CMD="$CMD --git-host \"$GIT_HOST\""
[ -n "$GIT_REPO_ID" ] && CMD="$CMD --git-repo-id \"$GIT_REPO_ID\""
[ -n "$GIT_USER_ID" ] && CMD="$CMD --git-user-id \"$GIT_USER_ID\""
[ -n "$HTTP_USER_AGENT" ] && CMD="$CMD --http-user-agent \"$HTTP_USER_AGENT\""

# Add flags
[ "$SKIP_OVERWRITE" = true ] && CMD="$CMD --skip-overwrite"
[ "$ENABLE_POST_PROCESS" = true ] && CMD="$CMD --enable-post-process-file"
[ "$DRY_RUN" = true ] && CMD="$CMD --dry-run"
[ "$MINIMAL_UPDATE" = true ] && CMD="$CMD --minimal-update"
[ "$VERBOSE" = true ] && CMD="$CMD --verbose"

# Build additional properties
PROPS="projectName=$PROJECT_NAME,packageName=$PACKAGE_NAME,packageVersion=$PACKAGE_VERSION,packageUrl=https://$GIT_HOST/$GIT_USER_ID/$GIT_REPO_ID"
if [ -n "$ADDITIONAL_PROPS" ]; then
    PROPS="$PROPS,$ADDITIONAL_PROPS"
fi
CMD="$CMD --additional-properties=\"$PROPS\""

# Execute the command
if [ "$VERBOSE" = true ]; then
    echo "🔧 Running command:"
    echo "$CMD"
    echo ""
fi

eval $CMD

if [ "$DRY_RUN" = true ]; then
    echo "🔍 Dry run complete - no files were generated"
    echo "Remove --dry-run flag to actually generate the client"
else
    echo "✅ ESI client generation complete!"
    echo "📂 Output directory: $OUTPUT_DIR"
    echo "📦 Package name: $PACKAGE_NAME"
    
    # Try to show generated file counts if possible
    if [ -d "$OUTPUT_DIR" ]; then
        if [ -d "$OUTPUT_DIR/src/api" ] || [ -d "$OUTPUT_DIR/api" ]; then
            API_DIR="$OUTPUT_DIR/src/api"
            [ ! -d "$API_DIR" ] && API_DIR="$OUTPUT_DIR/api"
            echo "🔧 APIs: $(find "$API_DIR" -name "*.py" 2>/dev/null | wc -l) API classes"
        fi
        
        if [ -d "$OUTPUT_DIR/src/models" ] || [ -d "$OUTPUT_DIR/models" ]; then
            MODEL_DIR="$OUTPUT_DIR/src/models"
            [ ! -d "$MODEL_DIR" ] && MODEL_DIR="$OUTPUT_DIR/models"
            echo "📋 Models: $(find "$MODEL_DIR" -name "*.py" 2>/dev/null | wc -l) data models"
        fi
    fi
fi