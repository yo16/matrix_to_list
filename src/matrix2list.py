""" matrix2list
"""

import os
import csv

def matrix2list(input_file_path, output_file_path, delimiter=',', skip_null_rec=True, null_str=''):
    """ マトリックス形式のcsvから、レコード形式のcsvへ置換する

    セルの中身は数値とは限らないので、ゴリゴリループを回すことにした。

    Parameters
    ------------------
    input_file_path: str
        入力ファイル(CSV)のパス。
    output_file_path: str
        出力ファイル(CSV)のパス。
    delimiter: str
        デリミター。csvだったら','だと思うけど、tsvも読みたくなるかもしれないし。
    skip_null_rec: bool
        空のセルをスキップするかどうか。
    null_str: str
        空のセルの定義。
        "-"とかありうる。
    """
    # 入力ファイルの存在チェック
    assert os.path.exists(input_file_path), f'入力ファイルがありません.({input_file_path})'

    # 出力フォルダがない場合は作成
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    # 開いて読む
    with open(input_file_path, 'r') as f:
        # delimiter	フィールド間を分割するのに使用する文字。	','(カンマ)
        # doublequote	フィールド内のquotecharがその文字自身である場合どのようにクオートするか。True の場合、この文字は二重化。 False の場合、 escapechar は quotechar の前に置かれます。	True
        # escapechar	エスケープ用の文字列をしてします。読み込み時、escapechar はそれに引き続く文字の特別な意味を取り除きます。	None
        # lineterminator	writerを使用する際に、各行の終端を表すのに使用する文字。readerでは、'\r' または '\n' を終端とするようにハードコードされているので関係ない。	'\r\n'
        # quotechar	delimiter や quotechar といった特殊文字を含むか、改行文字を含むフィールドをクオートする際に用いられる 1 文字からなる文字	'"'
        # skipinitialspace	True の場合、 delimiter の直後に続く空白は無視されます。	False
        reader = csv.reader(f, delimiter=',', doublequote=True, lineterminator='\r\n', quotechar='"', skipinitialspace=True)
        csv_data = [row for row in reader]
    # print(csv_data)

    # 列名を取得
    column1 = [ rec[0] for rec in csv_data[1:] ]
    column2 = csv_data[0][1:]
    len_column1 = len(column1)
    len_column2 = len(column2)
    # print(column1)
    # print(column2)

    # ヘッダー
    csv_data_out = []
    csv_data_out.append(['column1','column2','value'])

    # データ
    for rec in csv_data[1:]:
        col1 = rec[0]
        for i, val in enumerate(rec[1:]):
            csv_data_out.append([
                col1,
                column2[i%len_column2],
                val
            ])
    # print(csv_data_out)

    # 保存
    with open(output_file_path, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')    # オプションは必要だったらそのうち実装する
        writer.writerows(csv_data_out)
    
    return None
        



if __name__=="__main__":
    matrix2list('./input/sample.csv', './output/sample.csv')

    print('finished!')

