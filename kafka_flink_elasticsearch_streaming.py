from pyflink.table import TableEnvironment, EnvironmentSettings

# Create a TableEnvironment
env_settings = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env_settings)

# Specify connector and format jars
t_env.get_config().get_configuration().set_string(
    "pipeline.jars",
    "file:/home/laadaili/flink/lib/flink-sql-connector-kafka-3.0.2-1.18.jar;"
    "file:/home/laadaili/flink/lib/flink-sql-connector-elasticsearch7-3.0.1-1.17.jar"
)

# Define source table DDL
source_ddl = """
    CREATE TABLE source_table(
                    description VARCHAR,
                    title VARCHAR,
                    url VARCHAR,
                    author VARCHAR,
                    publishedAt VARCHAR,
                    content VARCHAR,
                    source_id VARCHAR,
                    source_name VARCHAR,
                    urlToImage VARCHAR
    ) WITH (
  'connector' = 'kafka',
        'topic' = 'topic_aya',
        'properties.bootstrap.servers' = 'localhost:9092',
        'properties.group.id' = 'test_3',
        'scan.startup.mode' = 'latest-offset',
        'format' = 'json'
    )
"""

# Define sink table DDL
sink_ddl = """
    CREATE TABLE sink_table(
                    description VARCHAR,
                    title VARCHAR,
                    url VARCHAR,
                    author VARCHAR,
                    publishedAt VARCHAR,
                    content VARCHAR,
                    source_id VARCHAR,
                    source_name VARCHAR,
                    urlToImage VARCHAR
    ) WITH (        
        'connector' = 'elasticsearch-7',
        'index' = 'demo_kafka_flink_streaming',
        'hosts' = 'localhost:9200',
        'format' = 'json'
    )
"""

# Execute DDL statements to create tables
t_env.execute_sql(source_ddl)
t_env.execute_sql(sink_ddl)

# Retrieve the source table
source_table = t_env.from_path('source_table')

print("Source Table Schema:")
source_table.print_schema()

# Process the data
result_table = source_table

# Retrieve the sink table
sink_table = t_env.from_path('sink_table')

print("Sink Table Schema:")
sink_table.print_schema()

# Insert the processed data into the sink table
result_table.execute_insert('sink_table').wait()

