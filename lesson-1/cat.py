import os
import sys

def merge_markdown(main_file, output_file):
    if not os.path.isfile(main_file):
        print(f"エラー: メインファイル '{main_file}' が存在しません。")
        sys.exit(1)
    
    with open(main_file, 'r', encoding='utf-8') as mf, open(output_file, 'w', encoding='utf-8') as of:
        lines = mf.readlines()
        for line_num, line in enumerate(lines, start=1):
            stripped_line = line.strip()
            if stripped_line.endswith('.md'):
                if os.path.isfile(stripped_line):
                    with open(stripped_line, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        of.write(content + '\n\n---\n\n')  # 水平線で区切る
                else:
                    print(f"エラー: 行 {line_num} で指定されたファイル '{stripped_line}' が存在しません。")
                    sys.exit(1)
            else:
                of.write(line)  # ヘッダーやその他の行をそのまま書き込む
    print(f"マージが完了しました。出力ファイル: {output_file}")

def main():
    # デフォルトのファイル名と出力ディレクトリ
    default_main = 'main.md'
    output_dir = 'output'
    default_output = os.path.join(output_dir, 'merged_output.md')  # 出力ファイルを 'output/merged_output.md' に設定
    
    # 出力ディレクトリが存在しない場合は作成
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 引数の数に応じてファイル名を設定
    if len(sys.argv) == 1:
        main_file = default_main
        output_file = default_output
    elif len(sys.argv) == 3:
        main_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        print("使用方法:")
        print("  python merge_markdown.py")
        print("      # デフォルトの 'main.md' を 'output/merged_output.md' にマージ")
        print("  python merge_markdown.py main.md output/merged.md")
        print("      # 指定したファイルをマージ（例: main.md を output/merged.md にマージ）")
        sys.exit(1)
    
    merge_markdown(main_file, output_file)

if __name__ == '__main__':
    main()
