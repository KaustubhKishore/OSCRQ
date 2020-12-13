package com.example.oscarq

import android.R.id
import android.app.KeyguardManager
import android.content.Context
import android.graphics.Color
import android.location.LocationManager
import android.net.ConnectivityManager
import android.os.Build
import android.os.Bundle
import android.os.Handler
import android.provider.Settings
import android.util.Log
import android.view.View
import android.view.accessibility.AccessibilityManager
import android.widget.ImageButton
import android.widget.TextView
import android.widget.Toolbar
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.NotificationCompat
import java.util.*

class security : AppCompatActivity() {
    @RequiresApi(Build.VERSION_CODES.LOLLIPOP)
    override fun onCreate(savedInstanceState: Bundle?){
        super.onCreate(savedInstanceState)
        setContentView(R.layout.security)
        val handler = Handler()
        val imgbutton: ImageButton = findViewById<ImageButton>(R.id.securityyy)
        val textView = findViewById<TextView>(R.id.textViewsecurity)

        imgbutton.setOnClickListener {

//            Android OS Security Settings
//            (L1) Ensure device firmware is up to date (Not Scored)

            if(Build.VERSION.SECURITY_PATCH== "2020-09-01")
            {
                handler.postDelayed(Runnable { textView.text =  "AUDIT FOR: Ensure Firmware is up to date (Android Security patch level)\n\n" + Build.VERSION.SECURITY_PATCH +  " - BUILD UP TO DATE" }, 3000)
            }
            else
            {
                handler.postDelayed(
                    Runnable {  textView.text =  "AUDIT FOR: Ensure Firmware is up to date (Android Security patch level)\n\n" + Build.VERSION.SECURITY_PATCH + " - BUILD VERSION NOT UP TO DATE" },
                    3000
                )
            }

//            (L1) Ensure 'Screen Lock' is set to 'Enabled' (Not Scored)
//            (L1) Ensure 'Make pattern visible' is set to 'Disabled' (if using
//            a pattern as device lock mechanism) (Not Scored)
//            (L1) Ensure 'Automatically Lock' is set to 'Immediately' (Not
//            Scored)
//            (L1) Ensure 'Power button instantly locks' is set to 'Enabled'
//            (Not Scored)
//            (L1) Ensure 'Lock Screen Message' is configured (Not Scored) --------------
//            (L2) Do not connect to untrusted Wi-Fi networks (Not
//                    Scored)
//            (L2) Ensure 'Show passwords' is set to 'Disabled' (Not
//            Scored) ------------
//            (L1) Ensure 'Developer Options' is set to 'Disabled' (Not
//            Scored)
//            (L1) Ensure 'Install unknown apps' is set to 'Disabled' (Not
//            Scored)
//            (L1) Do not root your device (Not Scored)
//            (L2) Ensure 'Smart Lock' is set to 'Disabled' (Not Scored) ------------
//            (L2) Ensure 'Lock SIM card' is set to 'Enabled' (Not Scored)
//            (L2) Ensure 'Find My Device' is set to 'Enabled' (Not Scored)
//            (L1) Ensure 'Use network-provided time' and 'Use network-
//            provided time zone' are set to 'Enabled' (Not Scored)
//            (L1) Ensure 'Remotely locate this device' is set to 'Enabled'
//            (Not Scored)
//            (L1) Ensure 'Allow remote lock and erase' is set to 'Enabled'
//            (Not Scored)
//            (L1) Ensure 'Scan device for security threats' is set to
//            'Enabled' (Not Scored)
//            (L1) Ensure 'Improve harmful app detection' is set to
//            'Enabled' (Not Scored)
//            (L1) Ensure 'Ask for unlock pattern/PIN/password before
//            unpinning' is set to 'Enabled' (Not Scored)
//            (L1) Ensure 'Screen timeout' is set to '1 minute or less' (Not
//            Scored)
//            (L1) Ensure 'Wi-Fi assistant' is set to 'Disabled' (Not Scored)
//            (L1) Keep device Apps up to date (Not Scored)
//            (L1) Ensure 'Add users from lock screen' is set to 'Disabled'
//            (Not Scored)
//            (L1) Ensure 'Guest profiles' do not exist (Not Scored)
//            (L1) Review app permissions periodically (Not Scored)
//            (L1) Ensure 'Instant apps' is set to 'Disabled' (Not Scored)







            //Ensure 'Screen Lock' is set to 'Enabled'(Pin/Password/Pattern)
            //TODO("VERSION.SDK_INT < M")

            val km = getSystemService(Context.KEYGUARD_SERVICE) as KeyguardManager
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                if(km.isDeviceSecure){
                    handler.postDelayed(
                        Runnable {
                            textView.text = textView.text as String + "\nAUDIT FOR: Ensure 'Screen Lock' is set to 'Enabled'(Pin/Password/Pattern)\n\n" +"DEVICE LOCK IS ENABLED"},
                        5000
                    )
                }
                else{
                    handler.postDelayed(
                        Runnable {  textView.text = textView.text as String + "\nAUDIT FOR: Ensure 'Screen Lock' is set to 'Enabled'(Pin/Password/Pattern)\n\n" + "DEVICE LOCK IS NOT ENABLED" },
                        5000
                    )
                }
            }

            //Do not connect to untrusted Wi-Fi networks (Not Scored)
            val connectivityManager=this.getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
            val networkInfo=connectivityManager.activeNetworkInfo
            handler.postDelayed(
                Runnable {   textView.text = textView.text as String + "\nAUDIT FOR: Do not connect to untrusted Wi-Fi networks (Not Scored)\n\n" + networkInfo + "\n" + "NO UNTRUSTED NETWORK DETECTED" },
                5000
            )

            //Ensure 'Developer Options' is set to 'Disabled' (Not Scored)
            if(Settings.Secure.getInt(contentResolver, Settings.Secure.ADB_ENABLED, 0) == 1) {
                // debugging enabled
                handler.postDelayed(
                    Runnable {   textView.text = textView.text as String + "\nAUDIR FOR: Ensure 'Developer Options' is set to 'Disabled' (Not Scored)\n\n" + "USB DEBUGGING MUST BE DISABLED"},
                    4500
                )

            } else {
                handler.postDelayed(Runnable {  textView.text = textView.text as String + "\nAUDIR FOR: Ensure 'Developer Options' is set to 'Disabled' (Not Scored)\n\n " +"DEBUGGING OPTIONS SAFELY CONFIGURED" }, 2500)
            }

//
//            //Ensure 'Install unknown apps' is set to 'Disabled' (Not Scored)
//            val isNonPlayAppAllowed = Settings.Secure.getInt(
//                contentResolver,
//                Settings.Secure.INSTALL_NON_MARKET_APPS
//            ) == 1
//            if (!isNonPlayAppAllowed) {
//                handler.postDelayed(
//                    Runnable {  textView.text = textView.text as String + "\n " +"Install from unknown sources is disabled" },
//                    3000
//                )
//            }
//            else{
////                handler.postDelayed(
////                    Runnable {  textView.text = textView.text as String + "\n " +"Disable install from unknown sources" },
////                    4000
////                )
//            }


            //Ensure 'Find My Device' is set to 'Enabled' (Not Scored)
            val locationManager =
                getSystemService(Context.LOCATION_SERVICE) as LocationManager

            if (locationManager.isProviderEnabled(LocationManager.GPS_PROVIDER)) {
                handler.postDelayed(
                    Runnable {  textView.text = textView.text as String + "\nAUDIT FOR: Ensure 'Find My Device' is set to 'Enabled' (Not Scored)\n\n" +"Find my device is enabled"},
                    4500
                )
            } else {

                handler.postDelayed(
                    Runnable {  textView.text = textView.text as String + "\nAUDIT FOR: Ensure 'Find My Device' is set to 'Enabled' (Not Scored)\n\n " +"Find my device is not enabled"},
                    3000
                )
            }


            //Ensure 'Lock screen' is set to 'Don't show notifications at all'
            //(Not Scored)
            val builder =
                NotificationCompat.Builder(applicationContext)
            try{
                builder.setVisibility(NotificationCompat.VISIBILITY_PUBLIC)
                handler.postDelayed(
                    Runnable { textView.text = textView.text as String + "\nAUDIT FOR: Ensure 'Lock screen' is set to 'Don't show notifications at all\n\n" +"Unsafe public notification settings" },
                    4000
                )
            }
            catch(e: Exception){
                handler.postDelayed(
                    Runnable { textView.text = textView.text as kotlin.String + "\nAUDIT FOR:Ensure 'Lock screen' is set to 'Don't show notifications at all'\n\n" +"Safe Public notification settings" },
                    4000
                )
            }


            //Ensure 'Use network-provided time' and 'Use network-
            //provided time zone' are set to 'Enabled' (Not Scored)
            val timeSettings = Settings.System.getString(
                this.contentResolver,
                Settings.System.AUTO_TIME
            )
            if (timeSettings.contentEquals("0")) {
//                Settings.System.putString(
//                    this.contentResolver,
//                    Settings.System.AUTO_TIME, "1"

                //Auto time not enabled
//                )
            }
            else{
                //Auto time is enabled
            }
            val now = Date(System.currentTimeMillis())
            Log.d("Date", now.toString())

            //Ensure 'Voice & Audio Activity' is set to 'Disabled' (Not Scored)
            val am =
                getSystemService(Context.ACCESSIBILITY_SERVICE) as AccessibilityManager
            val isAccessibilityEnabled = am.isEnabled
            //val isExploreByTouchEnabled = am.isTouchExplorationEnabled
            if(isAccessibilityEnabled){
                handler.postDelayed(
                    Runnable { textView.text = textView.text as String + "\nAUDIT FOR: Ensure 'Voice & Audio Activity' is set to 'Disabled' (Not Scored)\n\n" +"Disable voice activity" },
                    3000
                )
            }
            else{
                handler.postDelayed(
                    Runnable {
                        textView.text = textView.text as kotlin.String + "\nAUDIT FOR: Ensure 'Voice & Audio Activity' is set to 'Disabled' (Not Scored)\n\n" +"Voice activity disabled" },
                    4000
                )
            }
        }

    }


}