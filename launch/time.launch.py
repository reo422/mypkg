import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    
     timepublisher = launch_ros.actions.Node(
         package='mypkg',      #パッケージの名前を指定
         executable='timepublisher'   #実行するファイルの指定
         )
     timealert = launch_ros.actions.Node(
         package='mypkg',
         executable='timealert',
         output='screen'        #ログを端末に出すための設定
         )

     return launch.LaunchDescription([timepublisher, timealert])
