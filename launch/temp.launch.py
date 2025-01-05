import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    
     thermometer = launch_ros.actions.Node(
         package='mypkg',      #パッケージの名前を指定
         executable='thermometer'   #実行するファイルの指定
         )
     bodyalert = launch_ros.actions.Node(
         package='mypkg',
         executable='bodyalert',
         output='screen'        #ログを端末に出すための設定
         )

     return launch.LaunchDescription([thermometer, bodyalert])
