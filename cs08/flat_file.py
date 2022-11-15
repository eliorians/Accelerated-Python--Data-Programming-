
import pandas as pd

def main():
    #load files
    df_person = pd.read_csv('basic_person.csv', header=0)
    df_student = pd.read_csv('person_detail_f.csv', header=0)
    df_map = pd.read_csv('student_detail_v.csv', header=0)

    #process files
    df_map = df_map.groupby('student_id_new', as_index=False).max()
    
    df = df_map.merge(df_student)
    df = df.merge(df_person)

    #save file
    df.to_csv('joined.csv', index=False)

    # testing
    # print(df.info())
    # test = pd.read_csv('joined.csv')
    # print(test.iloc[:, :5].head(n=20))
    

if __name__ == '__main__':
    main()
