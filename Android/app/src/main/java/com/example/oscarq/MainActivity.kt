package com.example.oscarq
import android.app.KeyguardManager
import android.content.Context
import android.content.Intent
import android.location.LocationManager
import android.net.ConnectivityManager
import android.os.Build
import android.os.Bundle
import android.os.Handler
import android.provider.Settings
import android.util.Log
import android.view.View
import android.view.accessibility.AccessibilityManager
import android.widget.Button
import android.widget.ProgressBar
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.NotificationCompat
import com.mongodb.MongoClient
import com.mongodb.MongoClientURI
import java.util.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?){
        super.onCreate(savedInstanceState)

        try {
            this.supportActionBar!!.hide()
        } catch (e: NullPointerException) {
        }

        setContentView(R.layout.activity_main)
        findViewById<ProgressBar>(R.id.loadingPanel).visibility = View.GONE
        val handler = Handler()
        val button = findViewById<Button>(R.id.button)
        button.visibility = View.GONE
        val textView = findViewById<TextView>(R.id.textView0)
        val button2 = findViewById<Button>(R.id.button2)
//        val textView2 = findViewById<TextView>(R.id.textView2)
//        val textView3 = findViewById<TextView>(R.id.textView3)
        val button200 = findViewById<Button>(R.id.button200)

        val button420 = findViewById<Button>(R.id.button420)

        //TODO("adapt profiling and helper functions")
        //TODO("Mongo")
        //TODO("To add: L1/audit number corresponding to each audit")
        //TODO("Remove buttons and prototype UI and figure a new UI")

        //Ensure Firmware is up to date (Android Security patch level)
        //TODO("need to update latest patch automatically")

        button.setOnClickListener {
            findViewById<ProgressBar>(R.id.loadingPanel).visibility = View.VISIBLE
            if(Build.VERSION.SECURITY_PATCH== "2020-09-01")
            {
                handler.postDelayed(Runnable { textView.text =  "AUDIT FOR: Ensure Firmware is up to date (Android Security patch level)\n" + Build.VERSION.SECURITY_PATCH +  " - BUILD UP TO DATE" }, 3000)
            }
            else
            {
                handler.postDelayed(
                    Runnable {  textView.text =  "AUDIT FOR: Ensure Firmware is up to date (Android Security patch level)\n" + Build.VERSION.SECURITY_PATCH + " - BUILD VERSION NOT UP TO DATE" },
                    3000
                )
                findViewById<ProgressBar>(R.id.loadingPanel).visibility = View.GONE
            }

            //Ensure 'Screen Lock' is set to 'Enabled'(Pin/Password/Pattern)
            //TODO("VERSION.SDK_INT < M")

            val km = getSystemService(Context.KEYGUARD_SERVICE) as KeyguardManager
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                if(km.isDeviceSecure){
                    handler.postDelayed(
                        Runnable {
                            textView.text = textView.text as String + "\nAUDIT FOR: Ensure 'Screen Lock' is set to 'Enabled'(Pin/Password/Pattern)\n" +"DEVICE LOCK IS ENABLED"},
                        5000
                    )
                }
                else{
                    handler.postDelayed(
                        Runnable {  textView.text = textView.text as String + "\nAUDIT FOR: Ensure 'Screen Lock' is set to 'Enabled'(Pin/Password/Pattern)\n" + "DEVICE LOCK IS NOT ENABLED" },
                        5000
                    )
                }
            }

            //findViewById<ProgressBar>(R.id.loadingPanel).visibility = View.VISIBLE
            //Ensure 'Make pattern visible' is set to 'Disabled' (if using a
            //pattern as device lock mechanism)
            //TODO("How to check if pattern is not visible")

//            val locktype: Int = Locktype.getCurrent(contentResolver)
//            when (locktype) {
//                Locktype.PATTERN -> {  textView.text = textView.text as String + "\n" + "COULD NOT DETECT IS PATTERN IS SET TO NOT VISIBLE"
//                }
//            }
//
//            //Ensure 'Automatically Lock' is set to 'Immediately'
//            lateinit var dpm: DevicePolicyManager
//            lateinit var deviceAdminSample: ComponentName
//            //val timeMs: Long = 1000L * timeout.text.toString().toLong()
//            //dpm.setMaximumTimeToLock(deviceAdminSample, 1)
//            if(if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
//                    dpm.autoTimeRequired
//                } else {
//                    TODO("VERSION.SDK_INT < LOLLIPOP")
//                }
//            ){
//                textView.text = textView.text as String + "\n" + "KINDLY SET AUTOMOTIC TIME TO 1ms"
//            }
//            else{
//                textView.text = textView.text as String + "\n" + "AUTOMATIC LOCK IS SET TO MINIMUM DURATION"
//            }


            //Do not connect to untrusted Wi-Fi networks (Not Scored)
            val connectivityManager=this.getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
            val networkInfo=connectivityManager.activeNetworkInfo
            handler.postDelayed(
                Runnable {   textView.text = textView.text as String + "\nAUDIT FOR: Do not connect to untrusted Wi-Fi networks (Not Scored)\n" + networkInfo + "\n" + "NO UNTRUSTED NETWORK DETECTED" },
                5000
            )

            findViewById<ProgressBar>(R.id.loadingPanel).visibility = View.GONE

            //Ensure 'Developer Options' is set to 'Disabled' (Not Scored)
            if(Settings.Secure.getInt(contentResolver, Settings.Secure.ADB_ENABLED, 0) == 1) {
                // debugging enabled
                handler.postDelayed(
                    Runnable {   textView.text = textView.text as String + "\nAUDIR FOR: Ensure 'Developer Options' is set to 'Disabled' (Not Scored)\n" + "USB DEBUGGING MUST BE DISABLED"},
                    4500
                )

            } else {
                handler.postDelayed(Runnable {  textView.text = textView.text as String + "\nAUDIR FOR: Ensure 'Developer Options' is set to 'Disabled' (Not Scored)\n " +"DEBUGGING OPTIONS SAFELY CONFIGURED" }, 2500)
            }



            //Ensure 'Install unknown apps' is set to 'Disabled' (Not Scored)
            val isNonPlayAppAllowed = Settings.Secure.getInt(
                contentResolver,
                Settings.Secure.INSTALL_NON_MARKET_APPS
            ) == 1
            if (!isNonPlayAppAllowed) {
                handler.postDelayed(
                    Runnable {  textView.text = textView.text as String + "\n " +"Install from unknown sources is disabled" },
                    3000
                )
            }
            else{
                handler.postDelayed(
                    Runnable {  textView.text = textView.text as String + "\n " +"Disable install from unknown sources" },
                    4000
                )
            }


            //Ensure 'Find My Device' is set to 'Enabled' (Not Scored)
            val locationManager =
                getSystemService(Context.LOCATION_SERVICE) as LocationManager

            if (locationManager.isProviderEnabled(LocationManager.GPS_PROVIDER)) {
                handler.postDelayed(
                    Runnable {  textView.text = textView.text as String + "\nAUDIT FOR: Ensure 'Find My Device' is set to 'Enabled' (Not Scored)\n" +"Find my device is enabled"},
                    4500
                )
            } else {

                handler.postDelayed(
                    Runnable {  textView.text = textView.text as String + "\nAUDIT FOR: Ensure 'Find My Device' is set to 'Enabled' (Not Scored)\n " +"Find my device is not enabled"},
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
                    Runnable { textView.text = textView.text as String + "\nAUDIT FOR: Ensure 'Lock screen' is set to 'Don't show notifications at all\n" +"Unsafe public notification settings" },
                    4000
                )
            }
            catch(e: Exception){
                handler.postDelayed(
                    Runnable { textView.text = textView.text as kotlin.String + "\nAUDIT FOR:Ensure 'Lock screen' is set to 'Don't show notifications at all'\n" +"Safe Public notification settings" },
                    4000
                )
            }

            //(L1) Do not root your device (Not Scored)
//            val rootBeer = RootBeer(context)
//            if (rootBeer.isRooted()) {
//                handler.postDelayed(
//                    Runnable {  textView.text = textView.text as String + "\nAUDIT FOR: Do not root your device (Not Scored)\n " +"Indication of root"},
//                    3000
//                )
//            } else {
//                handler.postDelayed(
//                    Runnable {  textView.text = textView.text as String + "\nAUDIT FOR: Do not root your device (Not Scored)\n " +"Couldn't find indication of root"},
//                    3000
//                )
//            }


            //(L2) Ensure 'Lock SIM card' is set to 'Enabled' (Not Scored)

            /*
            * @return true if SIM card exists
            * false if SIM card is locked or doesn’t exists
            * Note: This method requires permissions “android.permission.READ_PHONE_STATE”
            */
            var isAvailable = false;
//            TelephonyManager telMgr = (TelephonyManager) mContext.getSystemService(Context.TELEPHONY_SERVICE);
//            val simState = telMgr.getSimState();
//            when(simState){
//                TelephonyManager.SIM_STATE_ABSENT ->//-> "SimState = “No Sim Found!”"
//                TelephonyManager.SIM_STATE_NETWORK_LOCKED  //Toast("SimState = “Network Locked!”")
//                TelephonyManager.SIM_STATE_PIN_REQUIRED -> //Toast("SimState = “PIN Required to access SIM!”")
//                TelephonyManager.SIM_STATE_PUK_REQUIRED  //Toast("SimState = “Network Locked!”")
//                TelephonyManager.SIM_STATE_READY -> isAvailable = true
//                TelephonyManager.SIM_STATE_UNKNOWN -> //toast("SimState = “Unknown SIM State!”")
//                else -> //toast("“Unknown SIM State!”")
//            }

            if(!isAvailable){
                //LOCK IS ENABLED
                handler.postDelayed(
                    Runnable { textView.text = textView.text as String + "\nAUDIT FOR: Ensure 'Lock SIM card' is set to 'Enabled' (Not Scored)\n" +"Lock is Enabled" },
                    3000
                )
            }
            else{
                //LOCK NOT ENABLED
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

            //Ensure 'Allow remote lock and erase' is set to 'Enabled'
            //(Not Scored)



            //Ensure 'Scan device for security threats' is set to
            //'Enabled' (Not Scored)
//            SafetyNet.getClient(this)
//                .isVerifyAppsEnabled()
//                .addOnCompleteListener(object : OnCompleteListener<VerifyAppsUserResponse?>() {
//                    fun onComplete(task: Task<VerifyAppsUserResponse?>) {
//                        if (task.isSuccessful()) {
//                            val result: VerifyAppsUserResponse = task.getResult()
//                            if (result.isVerifyAppsEnabled()) {
//                                Log.d(
//                                    "MY_APP_TAG",
//                                    "The Verify Apps feature is enabled."
//                                )
//                            } else {
//                                Log.d(
//                                    "MY_APP_TAG",
//                                    "The Verify Apps feature is disabled."
//                                )
//                            }
//                        } else {
//                            Log.e("MY_APP_TAG", "A general error occurred.")
//                        }
//                    }
//                })

            //Ensure 'Voice & Audio Activity' is set to 'Disabled' (Not Scored)
            val am =
                getSystemService(Context.ACCESSIBILITY_SERVICE) as AccessibilityManager
            val isAccessibilityEnabled = am.isEnabled
            //val isExploreByTouchEnabled = am.isTouchExplorationEnabled
            if(isAccessibilityEnabled){
                handler.postDelayed(
                    Runnable { textView.text = textView.text as String + "\nAUDIT FOR: Ensure 'Voice & Audio Activity' is set to 'Disabled' (Not Scored)\n" +"Disable voice activity" },
                    3000
                )
            }
            else{
                handler.postDelayed(
                    Runnable {
                        textView.text = textView.text as kotlin.String + "\nAUDIT FOR: Ensure 'Voice & Audio Activity' is set to 'Disabled' (Not Scored)\n" +"Voice activity disabled" },
                    4000
                )
            }
        }
//        button.setOnClickListener {
//            Toast.makeText(this@MainActivity, "Performed Firmware Check", Toast.LENGTH_SHORT).show()
//            textView.text = Build.VERSION.RELEASE + " - UP TO DATE"
//        }
        button2.setOnClickListener {
            val intent = Intent(this, Main3Activity::class.java)
            startActivity(intent)
        }
        button200.setOnClickListener {
            val intent = Intent(this, security::class.java)
            startActivity(intent)
        }
        button420.setOnClickListener {
            val intent = Intent(this, Privacy::class.java)
            startActivity(intent)
        }
    }

}


/*
list = []

helper: print, mongo etc

fun audit12(name: String, age: Int): String {
    return "Happy ${age}th birthday, $name!"
}

Android OS Security Settings
(L1) Ensure device firmware is up to date (Not Scored)
(L1) Ensure 'Screen Lock' is set to 'Enabled' (Not Scored)
(L1) Ensure 'Make pattern visible' is set to 'Disabled' (if using
a pattern as device lock mechanism) (Not Scored)
(L1) Ensure 'Automatically Lock' is set to 'Immediately' (Not
Scored)
(L1) Ensure 'Power button instantly locks' is set to 'Enabled'
(Not Scored)
(L1) Ensure 'Lock Screen Message' is configured (Not Scored) --------------
(L2) Do not connect to untrusted Wi-Fi networks (Not
Scored)
(L2) Ensure 'Show passwords' is set to 'Disabled' (Not
Scored) ------------
(L1) Ensure 'Developer Options' is set to 'Disabled' (Not
Scored)
(L1) Ensure 'Install unknown apps' is set to 'Disabled' (Not
Scored)
(L1) Do not root your device (Not Scored)
(L2) Ensure 'Smart Lock' is set to 'Disabled' (Not Scored) ------------
(L2) Ensure 'Lock SIM card' is set to 'Enabled' (Not Scored)
(L2) Ensure 'Find My Device' is set to 'Enabled' (Not Scored)
(L1) Ensure 'Use network-provided time' and 'Use network-
provided time zone' are set to 'Enabled' (Not Scored)
(L1) Ensure 'Remotely locate this device' is set to 'Enabled'
(Not Scored)
(L1) Ensure 'Allow remote lock and erase' is set to 'Enabled'
(Not Scored)
(L1) Ensure 'Scan device for security threats' is set to
'Enabled' (Not Scored)
(L1) Ensure 'Improve harmful app detection' is set to
'Enabled' (Not Scored)
(L1) Ensure 'Ask for unlock pattern/PIN/password before
unpinning' is set to 'Enabled' (Not Scored)
(L1) Ensure 'Screen timeout' is set to '1 minute or less' (Not
Scored)
(L1) Ensure 'Wi-Fi assistant' is set to 'Disabled' (Not Scored)
(L1) Keep device Apps up to date (Not Scored)
(L1) Ensure 'Add users from lock screen' is set to 'Disabled'
(Not Scored)
(L1) Ensure 'Guest profiles' do not exist (Not Scored)
(L1) Review app permissions periodically (Not Scored)
(L1) Ensure 'Instant apps' is set to 'Disabled' (Not Scored)

Android OS Privacy Settings
(L1) Ensure 'Lock screen' is set to 'Don't show notifications at
all' (Not Scored)
(L2) Ensure 'Use location' is set to 'Disabled' (Not Scored)

(L2) Ensure 'Back up to Google Drive' is 'Disabled' (Not
Scored)

(L1) Ensure 'Web and App Activity' is set to 'Disabled' (Not
Scored)
(L1) Ensure 'Device Information' is set to 'Disabled' (Not
Scored)
(L1) Ensure 'Voice & Audio Activity' is set to 'Disabled' (Not
Scored)
(L1) Ensure 'YouTube Search History' is set to 'Disabled' (Not
Scored)
(L1) Ensure 'YouTube Watch History' is set to 'Disabled' (Not
Scored)
(L1) Ensure 'Google Location History' is set to 'Disabled' (Not
Scored)
(L1) Ensure 'Opt out of Ads Personalization' is set to 'Enabled'
(Not Scored)

Android OS Chrome Browser Settings
(L1) Ensure 'Microphone' is set to 'Enabled' (Not Scored)
(L1) Ensure 'Location' is set to 'Enabled' (Not Scored)
(L1) Ensure 'Allow third-party cookies' is set to 'Disabled'
(Not Scored)
(L1) Ensure 'Safe Browsing' is set to 'Enabled' (Not Scored)
(L2) Ensure 'Search and URL suggestions' is set to 'Disabled'
(Not Scored)
(L2) Ensure 'Do Not Track' is set to 'Enabled' (Not Scored)

 */