LOCAL_DIR = "/tmp/"
import airflow.hooks.S3_hook


file_name = LOCAL_DIR + '/rdStandarized-16Mai.csv'
# df.sort_values(['company', 'year', 'period'], inplace=True)
# df.to_csv(file_name, sep=';', index=False)
hook = airflow.hooks.S3_hook.S3Hook('airflow-s3')
hook.load_file(
    filename=file_name,
    key='rdStandarized-16Mai.csv',
    bucket_name='airflow-s3',
    replace=True,
  )

  # Load file of done OCR
try:
    obj = hook.get_key('rdStandarized-16Mai.csv', 'airflow-s3').get()
    df = pd.read_csv(obj["Body"], sep=',')
except:
    print("PCAZ: file doesn't exist")
