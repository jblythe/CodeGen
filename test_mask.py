from codegen_sources.preprocessing.lang_processors.java_processor import JavaProcessor

java_code = r"""class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}"""
java_processor = JavaProcessor(root_folder="tree-sitter")
tokenized_java_code = java_processor.tokenize_code(java_code)
print(tokenized_java_code)
