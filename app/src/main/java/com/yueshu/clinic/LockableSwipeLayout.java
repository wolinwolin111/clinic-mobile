package com.yueshu.clinic;

import android.content.Context;
import android.util.AttributeSet;

import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

/**
 * SwipeRefreshLayout that yields to inner page scrolling when the web page asks for it.
 *
 * The stock canChildScrollUp() only asks whether the direct child (the WebView) can scroll up.
 * A page with an open modal or an inner scrollable list reports scroll lock through
 * PullBridge.setLock(); while locked, this layout refuses to intercept the drag so the
 * WebView handles the gesture (modal list scrolling, form scrolling) instead of triggering
 * a native refresh.
 */
public class LockableSwipeLayout extends SwipeRefreshLayout {
    private volatile boolean pageLocked = false;

    public LockableSwipeLayout(Context context) {
        super(context);
    }

    public LockableSwipeLayout(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    public void setPageLocked(boolean locked) {
        pageLocked = locked;
    }

    @Override
    public boolean canChildScrollUp() {
        if (pageLocked) {
            return true;
        }
        return super.canChildScrollUp();
    }
}
